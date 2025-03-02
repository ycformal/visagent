import cv2
import os
import torch
import openai
import functools
import numpy as np
import face_detection
import io, tokenize
from augly.utils.base_paths import EMOJI_DIR
import augly.image as imaugs
from PIL import Image,ImageDraw,ImageFont,ImageFilter
from transformers import (ViltProcessor, ViltForQuestionAnswering, 
    OwlViTProcessor, OwlViTForObjectDetection,
    MaskFormerFeatureExtractor, MaskFormerForInstanceSegmentation,
    CLIPProcessor, CLIPModel, AutoProcessor, BlipForQuestionAnswering,
    AutoModelForCausalLM, Owlv2Processor, Owlv2ForObjectDetection,
    PaliGemmaForConditionalGeneration)
from diffusers import StableDiffusionInpaintPipeline
from nltk.stem import PorterStemmer
import copy
import math
import nltk

from .nms import nms
from vis_utils import html_embed_image, html_colored_span, vis_masks

nltk.download('punkt_tab') # If there's error message, just modify the package name according to what the error message says


def parse_step(step_str,partial=False):
    tokens = list(tokenize.generate_tokens(io.StringIO(step_str).readline))
    output_var = tokens[0].string
    step_name = tokens[2].string
    parsed_result = dict(
        output_var=output_var,
        step_name=step_name)
    if partial:
        return parsed_result

    arg_tokens = [token for token in tokens[4:-3] if token.string not in [',','=']]
    num_tokens = len(arg_tokens) // 2
    args = dict()
    for i in range(num_tokens):
        args[arg_tokens[2*i].string] = arg_tokens[2*i+1].string
    parsed_result['args'] = args
    return parsed_result


def html_step_name(content):
    step_name = html_colored_span(content, 'red')
    return f'<b>{step_name}</b>'


def html_output(content):
    output = html_colored_span(content, 'green')
    return f'<b>{output}</b>'


def html_var_name(content):
    var_name = html_colored_span(content, 'blue')
    return f'<b>{var_name}</b>'


def html_arg_name(content):
    arg_name = html_colored_span(content, 'darkorange')
    return f'<b>{arg_name}</b>'

    
class EvalInterpreter():
    step_name = 'EVAL'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        output_var = parse_result['output_var']
        step_input = eval(parse_result['args']['expr'])
        assert(step_name==self.step_name)
        return step_input, output_var
    
    def html(self,eval_expression,step_input,step_output,output_var):
        eval_expression = eval_expression.replace('{','').replace('}','')
        step_name = html_step_name(self.step_name)
        var_name = html_var_name(output_var)
        output = html_output(step_output)
        expr = html_arg_name('expression')
        return f"""<div>{var_name}={step_name}({expr}="{eval_expression}")={step_name}({expr}="{step_input}")={output}</div>"""

    def execute(self,prog_step,inspect=False):
        step_input, output_var = self.parse(prog_step)
        prog_state = dict()
        for var_name,var_value in prog_step.state.items():
            if isinstance(var_value,str):
                if var_value in ['yes','no']:
                    prog_state[var_name] = var_value=='yes'
                elif var_value.isdecimal():
                    prog_state[var_name] = var_value
                else:
                    prog_state[var_name] = f"'{var_value}'"
            else:
                prog_state[var_name] = var_value
        
        eval_expression = step_input

        if 'xor' in step_input:
            step_input = step_input.replace('xor','!=')

        step_input = step_input.format(**prog_state)
        step_output = eval(step_input)
        prog_step.state[output_var] = step_output
        if inspect:
            html_str = self.html(eval_expression, step_input, step_output, output_var)
            return step_output, html_str

        return step_output
    
class GetInterpreter():
    step_name = 'GET'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        output_var = parse_result['output_var']
        image_var = parse_result['args']['image']
        assert(step_name==self.step_name)
        return image_var, output_var
    
    def html(self,img,bounding_box,output_var):
        step_name = html_step_name(self.step_name)
        img_str = html_embed_image(img)
        bounding_box = html_output(bounding_box)
        output_var = html_var_name(output_var)
        image_arg = html_arg_name('image')
        return f"""<div>{output_var}={step_name}({image_arg}={img_str})={bounding_box}</div>"""

    def execute(self,prog_step,inspect=False):
        img_var, output_var = self.parse(prog_step)
        prog_state = dict()
        img = prog_step.state[img_var]

        bounding_box = [[0, 0, img.size[0] - 1, img.size[1] - 1]]

        prog_step.state[output_var] = bounding_box
        if inspect:
            html_str = self.html(img, bounding_box, output_var)
            return bounding_box, html_str

        return bounding_box

class GetTopInterpreter():
    step_name = 'GET_TOP'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        output_var = parse_result['output_var']
        image_var = parse_result['args']['image']
        assert(step_name==self.step_name)
        return image_var, output_var
    
    def html(self,img,bounding_box,output_var):
        step_name = html_step_name(self.step_name)
        img_str = html_embed_image(img)
        bounding_box = html_output(bounding_box)
        output_var = html_var_name(output_var)
        image_arg = html_arg_name('image')
        return f"""<div>{output_var}={step_name}({image_arg}={img_str})={bounding_box}</div>"""

    def execute(self,prog_step,inspect=False):
        img_var, output_var = self.parse(prog_step)
        prog_state = dict()
        img = prog_step.state[img_var]

        bounding_box = [[0, 0, img.size[0] - 1, int(img.size[1] / 2)]]

        prog_step.state[output_var] = bounding_box
        if inspect:
            html_str = self.html(img, bounding_box, output_var)
            return bounding_box, html_str

        return bounding_box
    
class GetBottomInterpreter():
    step_name = 'GET_BOTTOM'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        output_var = parse_result['output_var']
        image_var = parse_result['args']['image']
        assert(step_name==self.step_name)
        return image_var, output_var
    
    def html(self,img,bounding_box,output_var):
        step_name = html_step_name(self.step_name)
        img_str = html_embed_image(img)
        bounding_box = html_output(bounding_box)
        output_var = html_var_name(output_var)
        image_arg = html_arg_name('image')
        return f"""<div>{output_var}={step_name}({image_arg}={img_str})={bounding_box}</div>"""

    def execute(self,prog_step,inspect=False):
        img_var, output_var = self.parse(prog_step)
        prog_state = dict()
        img = prog_step.state[img_var]

        bounding_box = [[0, int(img.size[1] / 2), img.size[0] - 1, img.size[1] - 1]]

        prog_step.state[output_var] = bounding_box
        if inspect:
            html_str = self.html(img, bounding_box, output_var)
            return bounding_box, html_str

        return bounding_box

class GetLeftInterpreter():
    step_name = 'GET_LEFT'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        output_var = parse_result['output_var']
        image_var = parse_result['args']['image']
        assert(step_name==self.step_name)
        return image_var, output_var
    
    def html(self,img,bounding_box,output_var):
        step_name = html_step_name(self.step_name)
        img_str = html_embed_image(img)
        bounding_box = html_output(bounding_box)
        output_var = html_var_name(output_var)
        image_arg = html_arg_name('image')
        return f"""<div>{output_var}={step_name}({image_arg}={img_str})={bounding_box}</div>"""

    def execute(self,prog_step,inspect=False):
        img_var, output_var = self.parse(prog_step)
        prog_state = dict()
        img = prog_step.state[img_var]

        bounding_box = [[0, 0, int(img.size[0] / 2), img.size[1] - 1]]

        prog_step.state[output_var] = bounding_box
        if inspect:
            html_str = self.html(img, bounding_box, output_var)
            return bounding_box, html_str

        return bounding_box
    
class GetRightInterpreter():
    step_name = 'GET_RIGHT'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        output_var = parse_result['output_var']
        image_var = parse_result['args']['image']
        assert(step_name==self.step_name)
        return image_var, output_var
    
    def html(self,img,bounding_box,output_var):
        step_name = html_step_name(self.step_name)
        img_str = html_embed_image(img)
        bounding_box = html_output(bounding_box)
        output_var = html_var_name(output_var)
        image_arg = html_arg_name('image')
        return f"""<div>{output_var}={step_name}({image_arg}={img_str})={bounding_box}</div>"""

    def execute(self,prog_step,inspect=False):
        img_var, output_var = self.parse(prog_step)
        prog_state = dict()
        img = prog_step.state[img_var]

        bounding_box = [[int(img.size[0] / 2), 0, img.size[0] - 1, img.size[1] - 1]]

        prog_step.state[output_var] = bounding_box
        if inspect:
            html_str = self.html(img, bounding_box, output_var)
            return bounding_box, html_str

        return bounding_box


class ResultInterpreter():
    step_name = 'RESULT'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        output_var = parse_result['args']['var']
        assert(step_name==self.step_name)
        return output_var

    def html(self,output,output_var):
        step_name = html_step_name(self.step_name)
        output_var = html_var_name(output_var)
        if isinstance(output, Image.Image):
            output = html_embed_image(output,300)
        else:
            output = html_output(output)
            
        return f"""<div>{step_name} -> {output_var} -> {output}</div>"""

    def execute(self,prog_step,inspect=False):
        output_var = self.parse(prog_step)
        if output_var in prog_step.state:
            output = prog_step.state[output_var]
        else:
            output = eval(output_var)
        if inspect:
            html_str = self.html(output,output_var)
            return output, html_str

        return output

class AssignInterpreter():
    step_name = 'ASSIGN'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        output_var = parse_result['args']['var']
        new_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return output_var, new_var

    def html(self,output,output_var):
        step_name = html_step_name(self.step_name)
        output_var = html_var_name(output_var)
        if isinstance(output, Image.Image):
            output = html_embed_image(output,300)
        else:
            output = html_output(output)
            
        return f"""<div>{step_name} -> {output_var} -> {output}</div>"""

    def execute(self,prog_step,inspect=False):
        output_var, new_var = self.parse(prog_step)
        if output_var in prog_step.state:
            output = prog_step.state[output_var]
            prog_step.state[new_var] = output
        else:
            output = eval(output_var)
            prog_step.state[new_var] = output
        if inspect:
            html_str = self.html(output,output_var)
            return output, html_str

        return output


class VQAInterpreter():
    step_name = 'VQA'

    def __init__(self):
        print(f'Registering {self.step_name} step')
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.processor = [AutoProcessor.from_pretrained("Salesforce/blip-vqa-capfilt-large"), ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa"), AutoProcessor.from_pretrained("google/paligemma-3b-ft-vqav2-448")]
        self.model = [BlipForQuestionAnswering.from_pretrained(
            "Salesforce/blip-vqa-capfilt-large").to(self.device), ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa").to(self.device), PaliGemmaForConditionalGeneration.from_pretrained("google/paligemma-3b-ft-vqav2-448").to(self.device)]
        # self.processor = [AutoProcessor.from_pretrained("Salesforce/blip-vqa-capfilt-large")]
        # self.model = [BlipForQuestionAnswering.from_pretrained(
        #     "Salesforce/blip-vqa-capfilt-large").to(self.device)]
        for model in self.model:
            model.eval()
        self.stemmer = PorterStemmer()

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        args = parse_result['args']
        img_var = args['image']
        question = eval(args['question'])
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return img_var,question,output_var

    def predict(self,img,question):
        results = []
        for i in range(len(self.processor)):
            encoding = self.processor[i](img,question,return_tensors='pt')
            encoding = {k:v.to(self.device) for k,v in encoding.items()}
            with torch.no_grad():
                try:
                    outputs = self.model[i].generate(**encoding, max_new_tokens=50)
                    result = self.processor[i].decode(outputs[0], skip_special_tokens=True)
                    if question not in result:
                        results.append(result)
                    else:
                        result = result.replace(question,'').strip()
                        results.append(result)
                except:
                    try:
                        outputs = self.model[i](**encoding)
                        logits = outputs.logits
                        idx = logits.argmax(-1).item()
                        results.append(self.model[i].config.id2label[idx])
                    except:
                        print(question)
                        print('Model failed to generate answer. Update the code for VQA answer generation.')
                        results.append('Runtime error on this VQA model.')
        stemmed_results = [''] * len(results)
        for i in range(len(results)):
            words = nltk.word_tokenize(results[i].lower())
            stems = {self.stemmer.stem(word) for word in words if word.isalnum()}
            stemmed_results[i] = ' '.join(stems)

        votes = [0] * len(results)

        for i, stems_i in enumerate(stemmed_results):
            for j, stems_j in enumerate(stemmed_results):
                if i != j:
                    # Check if there is any overlap between the two sentences' stems
                    if set(stems_i.split()).intersection(set(stems_j.split())):
                        votes[i] += 1

        max_votes = max(votes)
        if max_votes == 0:
            return min(results, key=lambda x: len(x.split()))

        candidate_indices = [i for i, vote in enumerate(votes) if vote == max_votes]
        best_index = min(candidate_indices, key=lambda i: len(results[i].split()))
        return results[best_index]

    def html(self,img,question,answer,output_var):
        step_name = html_step_name(self.step_name)
        img_str = html_embed_image(img)
        answer = html_output(answer)
        output_var = html_var_name(output_var)
        image_arg = html_arg_name('image')
        question_arg = html_arg_name('question')
        return f"""<div>{output_var}={step_name}({image_arg}={img_str},&nbsp;{question_arg}='{question}')={answer}</div>"""

    def execute(self,prog_step,inspect=False):
        img_var,question,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        answer = self.predict(img,question)
        prog_step.state[output_var] = answer
        if inspect:
            html_str = self.html(img, question, answer, output_var)
            return answer, html_str

        return answer


class LocInterpreter():
    step_name = 'LOC'

    def __init__(self,thresh=0.1,nms_thresh=0.5):
        print(f'Registering {self.step_name} step')
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.processor = [OwlViTProcessor.from_pretrained(
            "google/owlvit-large-patch14"), Owlv2Processor.from_pretrained("google/owlv2-large-patch14"), Owlv2Processor.from_pretrained("google/owlv2-large-patch14-ensemble")]
        self.model = [OwlViTForObjectDetection.from_pretrained(
            "google/owlvit-large-patch14").to(self.device), Owlv2ForObjectDetection.from_pretrained("google/owlv2-large-patch14").to(self.device), Owlv2ForObjectDetection.from_pretrained("google/owlv2-large-patch14-ensemble").to(self.device)]
        for model in self.model:
            model.eval()
        self.thresh = thresh
        self.nms_thresh = nms_thresh
        self.torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        self.processor_cap = AutoProcessor.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)
        self.model_cap = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-large", torch_dtype=self.torch_dtype, trust_remote_code=True).to(self.device)
        self.model_cap.eval()
        self.processor_vqa = AutoProcessor.from_pretrained("Salesforce/blip-vqa-capfilt-large")
        self.model_vqa = BlipForQuestionAnswering.from_pretrained(
            "Salesforce/blip-vqa-capfilt-large").to(self.device)
        self.model_vqa.eval()

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        img_var = parse_result['args']['image']
        obj_name = eval(parse_result['args']['object'])
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return img_var,obj_name,output_var

    def normalize_coord(self,bbox,img_size):
        w,h = img_size
        x1,y1,x2,y2 = [int(v) for v in bbox]
        x1 = max(0,x1)
        y1 = max(0,y1)
        x2 = min(x2,w-1)
        y2 = min(y2,h-1)
        return [x1,y1,x2,y2]

    def predict(self,img,obj_name):
        boxes = []
        scores = []
        for i in range(len(self.processor)):
            encoding = self.processor[i](
                text=[[f'a photo of {obj_name}']], 
                images=img,
                return_tensors='pt')
            encoding = {k:v.to(self.device) for k,v in encoding.items()}
            with torch.no_grad():
                outputs = self.model[i](**encoding)
                for k,v in outputs.items():
                    if v is not None:
                        outputs[k] = v.to('cpu') if isinstance(v, torch.Tensor) else v
            
            target_sizes = torch.Tensor([img.size[::-1]])
            results = self.processor[i].post_process_object_detection(outputs=outputs,threshold=self.thresh,target_sizes=target_sizes)
            _boxes, _scores = results[0]["boxes"], results[0]["scores"]
            _boxes = _boxes.cpu().detach().numpy().tolist()
            _scores = _scores.cpu().detach().numpy().tolist()

            if len(_boxes) == 0:
                continue

            _boxes, _scores = zip(*sorted(zip(_boxes,_scores),key=lambda x: x[1],reverse=True))
            selected_boxes = []
            selected_scores = []
            for i in range(len(_scores)):
                if _scores[i] > self.thresh:
                    coord = self.normalize_coord(_boxes[i],img.size)
                    selected_boxes.append(coord)
                    selected_scores.append(_scores[i])

            selected_boxes, selected_scores = nms(
                selected_boxes,selected_scores,self.nms_thresh)
            boxes.extend(selected_boxes)
            scores.extend(selected_scores)

        if len(boxes) == 0:
            return []

        box_groups = []
        score_groups = []
        # boxes with IoU > 0.8 are in the same group
        for i in range(len(boxes)):
            found = False
            for j in range(len(box_groups)):
                for k in range(len(box_groups[j])):
                    x1 = max(boxes[i][0], box_groups[j][k][0])
                    y1 = max(boxes[i][1], box_groups[j][k][1])
                    x2 = min(boxes[i][2], box_groups[j][k][2])
                    y2 = min(boxes[i][3], box_groups[j][k][3])
                    if x1 < x2 and y1 < y2:
                        overlap_area = (x2 - x1) * (y2 - y1)
                        area1 = (boxes[i][2] - boxes[i][0]) * (boxes[i][3] - boxes[i][1])
                        area2 = (box_groups[j][k][2] - box_groups[j][k][0]) * (box_groups[j][k][3] - box_groups[j][k][1])
                        if overlap_area / (area1 + area2 - overlap_area) > 0.8 and k == len(box_groups[j]) - 1:
                            box_groups[j].append(boxes[i])
                            score_groups[j].append(scores[i])
                            found = True
                            break
                        elif overlap_area / (area1 + area2 - overlap_area) <= 0.8:
                            break
                if found:
                    break
            if not found:
                box_groups.append([boxes[i]])
                score_groups.append([scores[i]])

        # only keep groups with total score > math.ceil(len(self.processor) / 2) * self.thresh
        selected_boxes = []
        selected_scores = []
        for i in range(len(box_groups)):
            total_score = sum(score_groups[i])
            if total_score > math.ceil(len(self.processor) / 2) * self.thresh:
                selected_boxes.append(box_groups[i])
                selected_scores.append(sum(score_groups[i]) / len(score_groups[i]))

        if len(selected_boxes) == 0:
            return []
        
        for i in range(len(selected_boxes)):
            min_x = min([j[0] for j in selected_boxes[i]])
            min_y = min([j[1] for j in selected_boxes[i]])
            max_x = max([j[2] for j in selected_boxes[i]])
            max_y = max([j[3] for j in selected_boxes[i]])
            selected_boxes[i] = [min_x, min_y, max_x, max_y]

        # sort by score
        selected_boxes, selected_scores = zip(*sorted(zip(selected_boxes, selected_scores), key=lambda x: x[1], reverse=True))
        return selected_boxes

    def top_box(self,img):
        w,h = img.size        
        return [0,0,w-1,int(h/2)]

    def bottom_box(self,img):
        w,h = img.size
        return [0,int(h/2),w-1,h-1]

    def left_box(self,img):
        w,h = img.size
        return [0,0,int(w/2),h-1]

    def right_box(self,img):
        w,h = img.size
        return [int(w/2),0,w-1,h-1]

    def box_image(self,img,boxes,highlight_best=True):
        img1 = img.copy()
        draw = ImageDraw.Draw(img1)
        for i,box in enumerate(boxes):
            if i==0 and highlight_best:
                color = 'red'
            else:
                color = 'blue'

            draw.rectangle(box,outline=color,width=5)

        return img1

    def html(self,img,box_img,output_var,obj_name):
        step_name=html_step_name(self.step_name)
        obj_arg=html_arg_name('object')
        img_arg=html_arg_name('image')
        output_var=html_var_name(output_var)
        img=html_embed_image(img)
        box_img=html_embed_image(box_img,300)
        return f"<div>{output_var}={step_name}({img_arg}={img}, {obj_arg}='{obj_name}')={box_img}</div>"
    
    def get_caption(self,img):
        prompt = "<MORE_DETAILED_CAPTION>"
        inputs = self.processor_cap(text=prompt, images=img, return_tensors="pt").to(self.device, self.torch_dtype)
        generated_ids = self.model_cap.generate(
            input_ids=inputs["input_ids"],
            pixel_values=inputs["pixel_values"],
            max_new_tokens=1024,
            num_beams=3,
            do_sample=False
        )
        generated_text = self.processor_cap.batch_decode(generated_ids, skip_special_tokens=False)[0]
        parsed_answer = self.processor_cap.post_process_generation(generated_text, task="<MORE_DETAILED_CAPTION>", image_size=(img.width, img.height))
        return parsed_answer['<MORE_DETAILED_CAPTION>']
    
    def get_vqa(self,img,question):
        encoding = self.processor_vqa(img,question,return_tensors='pt')
        encoding = {k:v.to(self.device) for k,v in encoding.items()}
        with torch.no_grad():
            outputs = self.model_vqa.generate(**encoding)
        
        return self.processor_vqa.decode(outputs[0], skip_special_tokens=True)


    def execute(self,prog_step,inspect=False):
        img_var,obj_name,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        if obj_name=='TOP':
            bboxes = [self.top_box(img)]
        elif obj_name=='BOTTOM':
            bboxes = [self.bottom_box(img)]
        elif obj_name=='LEFT':
            bboxes = [self.left_box(img)]
        elif obj_name=='RIGHT':
            bboxes = [self.right_box(img)]
        else:
            bboxes = self.predict(img,obj_name)

        parse_result = parse_step(prog_step.prog_str)
        if 'plural' in parse_result['args'] and len(bboxes) > 0 and eval(parse_result['args']['plural'])==True:
            bboxes = [[0, 0, img.size[0] - 1, img.size[1] - 1]]

        box_img = self.box_image(img, bboxes)
        prog_step.state[output_var] = bboxes
        prog_step.state[output_var+'_IMAGE'] = box_img
        if inspect:
            html_str = self.html(img, box_img, output_var, obj_name)
            return bboxes, html_str

        return bboxes

# uncomment the following if you want to test Visprog
# class LocInterpreter():
#     step_name = 'LOC'

#     def __init__(self,thresh=0.1,nms_thresh=0.5):
#         print(f'Registering {self.step_name} step')
#         self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
#         self.processor = OwlViTProcessor.from_pretrained(
#             "google/owlvit-large-patch14")
#         self.model = OwlViTForObjectDetection.from_pretrained(
#             "google/owlvit-large-patch14").to(self.device)
#         self.model.eval()
#         self.thresh = thresh
#         self.nms_thresh = nms_thresh

#     def parse(self,prog_step):
#         parse_result = parse_step(prog_step.prog_str)
#         step_name = parse_result['step_name']
#         img_var = parse_result['args']['image']
#         obj_name = eval(parse_result['args']['object'])
#         output_var = parse_result['output_var']
#         assert(step_name==self.step_name)
#         return img_var,obj_name,output_var

#     def normalize_coord(self,bbox,img_size):
#         w,h = img_size
#         x1,y1,x2,y2 = [int(v) for v in bbox]
#         x1 = max(0,x1)
#         y1 = max(0,y1)
#         x2 = min(x2,w-1)
#         y2 = min(y2,h-1)
#         return [x1,y1,x2,y2]

#     def predict(self,img,obj_name):
#         encoding = self.processor(
#             text=[[f'a photo of {obj_name}']], 
#             images=img,
#             return_tensors='pt')
#         encoding = {k:v.to(self.device) for k,v in encoding.items()}
#         with torch.no_grad():
#             outputs = self.model(**encoding)
#             for k,v in outputs.items():
#                 if v is not None:
#                     outputs[k] = v.to('cpu') if isinstance(v, torch.Tensor) else v
        
#         target_sizes = torch.Tensor([img.size[::-1]])
#         results = self.processor.post_process_object_detection(outputs=outputs,threshold=self.thresh,target_sizes=target_sizes)
#         boxes, scores = results[0]["boxes"], results[0]["scores"]
#         boxes = boxes.cpu().detach().numpy().tolist()
#         scores = scores.cpu().detach().numpy().tolist()
#         if len(boxes)==0:
#             return []

#         boxes, scores = zip(*sorted(zip(boxes,scores),key=lambda x: x[1],reverse=True))
#         selected_boxes = []
#         selected_scores = []
#         for i in range(len(scores)):
#             if scores[i] > self.thresh:
#                 coord = self.normalize_coord(boxes[i],img.size)
#                 selected_boxes.append(coord)
#                 selected_scores.append(scores[i])

#         selected_boxes, selected_scores = nms(
#             selected_boxes,selected_scores,self.nms_thresh)
#         return selected_boxes

#     def top_box(self,img):
#         w,h = img.size        
#         return [0,0,w-1,int(h/2)]

#     def bottom_box(self,img):
#         w,h = img.size
#         return [0,int(h/2),w-1,h-1]

#     def left_box(self,img):
#         w,h = img.size
#         return [0,0,int(w/2),h-1]

#     def right_box(self,img):
#         w,h = img.size
#         return [int(w/2),0,w-1,h-1]

#     def box_image(self,img,boxes,highlight_best=True):
#         img1 = img.copy()
#         draw = ImageDraw.Draw(img1)
#         for i,box in enumerate(boxes):
#             if i==0 and highlight_best:
#                 color = 'red'
#             else:
#                 color = 'blue'

#             draw.rectangle(box,outline=color,width=5)

#         return img1

#     def html(self,img,box_img,output_var,obj_name):
#         step_name=html_step_name(self.step_name)
#         obj_arg=html_arg_name('object')
#         img_arg=html_arg_name('image')
#         output_var=html_var_name(output_var)
#         img=html_embed_image(img)
#         box_img=html_embed_image(box_img,300)
#         return f"<div>{output_var}={step_name}({img_arg}={img}, {obj_arg}='{obj_name}')={box_img}</div>"


#     def execute(self,prog_step,inspect=False):
#         img_var,obj_name,output_var = self.parse(prog_step)
#         img = prog_step.state[img_var]
#         if obj_name=='TOP':
#             bboxes = [self.top_box(img)]
#         elif obj_name=='BOTTOM':
#             bboxes = [self.bottom_box(img)]
#         elif obj_name=='LEFT':
#             bboxes = [self.left_box(img)]
#         elif obj_name=='RIGHT':
#             bboxes = [self.right_box(img)]
#         else:
#             bboxes = self.predict(img,obj_name)

#         box_img = self.box_image(img, bboxes)
#         prog_step.state[output_var] = bboxes
#         prog_step.state[output_var+'_IMAGE'] = box_img
#         if inspect:
#             html_str = self.html(img, box_img, output_var, obj_name)
#             return bboxes, html_str

#         return bboxes
    
class MergeInterpreter():
    step_name = 'MERGE'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        box_var = parse_result['args']['box']
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return box_var,output_var
    
    def html(self,boxes,merged,output_var):
        step_name = html_step_name(self.step_name)
        output_var = html_var_name(output_var)
        return f"""<div>{output_var}={step_name}({boxes})={merged}</div>"""
    
    def execute(self,prog_step,inspect=False):
        box_var,output_var = self.parse(prog_step)
        if box_var in prog_step.state:
            boxes = prog_step.state[box_var]
        else:
            boxes = eval(eval(box_var))
        
        min_x = min([box[0] for box in boxes])
        min_y = min([box[1] for box in boxes])
        max_x = max([box[2] for box in boxes])
        max_y = max([box[3] for box in boxes])
        merged = [min_x,min_y,max_x,max_y]
        
        prog_step.state[output_var] = merged
        if inspect:
            html_str = self.html(boxes, merged, output_var)
            return merged, html_str

        return merged
    
class CapInterpreter():
    step_name = 'CAP'

    def __init__(self):
        print(f'Registering {self.step_name} step')
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        self.processor = AutoProcessor.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-large", torch_dtype=self.torch_dtype, trust_remote_code=True).to(self.device)
        self.model.eval()

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        img_var = parse_result['args']['image']
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return img_var,output_var

    def predict(self,img):
        prompt = "<MORE_DETAILED_CAPTION>"
        inputs = self.processor(text=prompt, images=img, return_tensors="pt").to(self.device, self.torch_dtype)
        generated_ids = self.model.generate(
            input_ids=inputs["input_ids"],
            pixel_values=inputs["pixel_values"],
            max_new_tokens=1024,
            num_beams=3,
            do_sample=False
        )
        generated_text = self.processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
        parsed_answer = self.processor.post_process_generation(generated_text, task="<MORE_DETAILED_CAPTION>", image_size=(img.width, img.height))
        return parsed_answer['<MORE_DETAILED_CAPTION>']

    def html(self,img,output,output_var):
        step_name = html_step_name(self.step_name)
        img_str = html_embed_image(img)
        output = html_output(output)
        output_var = html_var_name(output_var)
        image_arg = html_arg_name('image')
        return f"""<div>{output_var}={step_name}({image_arg}={img_str})={output}</div>"""

    def execute(self,prog_step,inspect=False):
        img_var,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        caption = self.predict(img)
        prog_step.state[output_var] = caption
        if inspect:
            html_str = self.html(img, caption, output_var)
            return caption, html_str

        return caption


class Loc2Interpreter(LocInterpreter):

    def execute(self,prog_step,inspect=False):
        img_var,obj_name,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        bboxes = self.predict(img,obj_name)

        objs = []
        for box in bboxes:
            objs.append(dict(
                box=box,
                category=obj_name
            ))
        prog_step.state[output_var] = objs

        if inspect:
            box_img = self.box_image(img, bboxes, highlight_best=False)
            html_str = self.html(img, box_img, output_var, obj_name)
            return bboxes, html_str

        return objs


class CountInterpreter():
    step_name = 'COUNT'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        box_var = parse_result['args']['box']
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return box_var,output_var

    def html(self,box_img,output_var,count):
        step_name = html_step_name(self.step_name)
        output_var = html_var_name(output_var)
        box_arg = html_arg_name('bbox')
        box_img = html_embed_image(box_img)
        output = html_output(count)
        return f"""<div>{output_var}={step_name}({box_arg}={box_img})={output}</div>"""

    def execute(self,prog_step,inspect=False):
        box_var,output_var = self.parse(prog_step)
        boxes = prog_step.state[box_var]
        count = len(boxes)
        prog_step.state[output_var] = count
        if inspect:
            box_img = None
            try:
                box_img = prog_step.state[box_var+'_IMAGE']
            except:
                box_img = Image.new('RGB',(100,100),'black')
            html_str = self.html(box_img, output_var, count)
            return count, html_str

        return count


class CropInterpreter():
    step_name = 'CROP'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def expand_box(self,box,img_size,factor=1.5):
        W,H = img_size
        x1,y1,x2,y2 = box
        dw = int(factor*(x2-x1)/2)
        dh = int(factor*(y2-y1)/2)
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)
        x1 = max(0,cx - dw)
        x2 = min(cx + dw,W)
        y1 = max(0,cy - dh)
        y2 = min(cy + dh,H)
        return [x1,y1,x2,y2]

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        img_var = parse_result['args']['image']
        box_var = parse_result['args']['box']
        index = 0
        if 'index' in parse_result['args']:
            index = int(parse_result['args']['index'])
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return img_var,box_var,index,output_var

    def html(self,img,out_img,output_var,box_img):
        img = html_embed_image(img)
        out_img = html_embed_image(out_img,300)
        box_img = html_embed_image(box_img)
        output_var = html_var_name(output_var)
        step_name = html_step_name(self.step_name)
        box_arg = html_arg_name('bbox')
        return f"""<div>{output_var}={step_name}({box_arg}={box_img})={out_img}</div>"""

    def execute(self,prog_step,inspect=False):
        img_var,box_var,index,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        boxes = prog_step.state[box_var]
        if len(boxes) > 0:
            box = boxes[index]
            box = self.expand_box(box, img.size)
            out_img = img.crop(box)
        else:
            box = []
            out_img = img

        prog_step.state[output_var] = out_img
        if inspect:
            box_img = None
            try:
                box_img = prog_step.state[box_var+'_IMAGE']
            except:
                box_img = img
            html_str = self.html(img, out_img, output_var, box_img)
            return out_img, html_str

        return out_img


class CropRightOfInterpreter(CropInterpreter):
    step_name = 'CROP_RIGHTOF'

    def right_of(self,box,img_size):
        w,h = img_size
        x1,y1,x2,y2 = box
        cx = int((x1+x2)/2)
        return [cx,0,w-1,h-1]

    def execute(self,prog_step,inspect=False):
        img_var,box_var,index,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        boxes = prog_step.state[box_var]
        if len(boxes) > 0:
            box = boxes[index]
            right_box = self.right_of(box, img.size)
        else:
            w,h = img.size
            box = []
            right_box = [int(w/2),0,w-1,h-1]
        
        out_img = img.crop(right_box)

        prog_step.state[output_var] = out_img
        if inspect:
            box_img = None
            try:
                box_img = prog_step.state[box_var+'_IMAGE']
            except:
                box_img = img
            html_str = self.html(img, out_img, output_var, box_img)
            return out_img, html_str

        return out_img


class CropLeftOfInterpreter(CropInterpreter):
    step_name = 'CROP_LEFTOF'

    def left_of(self,box,img_size):
        w,h = img_size
        x1,y1,x2,y2 = box
        cx = int((x1+x2)/2)
        return [0,0,cx,h-1]

    def execute(self,prog_step,inspect=False):
        img_var,box_var,index,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        boxes = prog_step.state[box_var]
        if len(boxes) > 0:
            box = boxes[index]
            left_box = self.left_of(box, img.size)
        else:
            w,h = img.size
            box = []
            left_box = [0,0,int(w/2),h-1]
        
        out_img = img.crop(left_box)

        prog_step.state[output_var] = out_img
        if inspect:
            box_img = None
            try:
                box_img = prog_step.state[box_var+'_IMAGE']
            except:
                box_img = img
            html_str = self.html(img, out_img, output_var, box_img)
            return out_img, html_str

        return out_img


class CropAboveInterpreter(CropInterpreter):
    step_name = 'CROP_ABOVE'

    def above(self,box,img_size):
        w,h = img_size
        x1,y1,x2,y2 = box
        cy = int((y1+y2)/2)
        return [0,0,w-1,cy]

    def execute(self,prog_step,inspect=False):
        img_var,box_var,index,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        boxes = prog_step.state[box_var]
        if len(boxes) > 0:
            box = boxes[index]
            above_box = self.above(box, img.size)
        else:
            w,h = img.size
            box = []
            above_box = [0,0,int(w/2),h-1]
        
        out_img = img.crop(above_box)

        prog_step.state[output_var] = out_img
        if inspect:
            box_img = None
            try:
                box_img = prog_step.state[box_var+'_IMAGE']
            except:
                box_img = img
            html_str = self.html(img, out_img, output_var, box_img)
            return out_img, html_str

        return out_img

class CropBelowInterpreter(CropInterpreter):
    step_name = 'CROP_BELOW'

    def below(self,box,img_size):
        w,h = img_size
        x1,y1,x2,y2 = box
        cy = int((y1+y2)/2)
        return [0,cy,w-1,h-1]

    def execute(self,prog_step,inspect=False):
        img_var,box_var,index,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        boxes = prog_step.state[box_var]
        if len(boxes) > 0:
            box = boxes[index]
            below_box = self.below(box, img.size)
        else:
            w,h = img.size
            box = []
            below_box = [0,0,int(w/2),h-1]
        
        out_img = img.crop(below_box)

        prog_step.state[output_var] = out_img
        if inspect:
            box_img = None
            try:
                box_img = prog_step.state[box_var+'_IMAGE']
            except:
                box_img = img
            html_str = self.html(img, out_img, output_var, box_img)
            return out_img, html_str

        return out_img

class CropFrontOfInterpreter(CropInterpreter):
    step_name = 'CROP_FRONTOF'

class CropInFrontInterpreter(CropInterpreter):
    step_name = 'CROP_INFRONT'

class CropInFrontOfInterpreter(CropInterpreter):
    step_name = 'CROP_INFRONTOF'

class CropBehindInterpreter(CropInterpreter):
    step_name = 'CROP_BEHIND'


class CropAheadInterpreter(CropInterpreter):
    step_name = 'CROP_AHEAD'


class SegmentInterpreter():
    step_name = 'SEG'

    def __init__(self):
        print(f'Registering {self.step_name} step')
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.feature_extractor = MaskFormerFeatureExtractor.from_pretrained(
            "facebook/maskformer-swin-base-coco")
        self.model = MaskFormerForInstanceSegmentation.from_pretrained(
            "facebook/maskformer-swin-base-coco").to(self.device)
        self.model.eval()

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        img_var = parse_result['args']['image']
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return img_var,output_var

    def pred_seg(self,img):
        inputs = self.feature_extractor(images=img, return_tensors="pt")
        inputs = {k:v.to(self.device) for k,v in inputs.items()}
        with torch.no_grad():
            outputs = self.model(**inputs)
        outputs = self.feature_extractor.post_process_panoptic_segmentation(outputs)[0]
        instance_map = outputs['segmentation'].cpu().numpy()
        objs = []
        print(outputs.keys())
        for seg in outputs['segments_info']:
            inst_id = seg['id']
            label_id = seg['label_id']
            category = self.model.config.id2label[label_id]
            mask = (instance_map==inst_id).astype(float)
            resized_mask = np.array(
                Image.fromarray(mask).resize(
                    img.size,resample=Image.BILINEAR))
            Y,X = np.where(resized_mask>0.5)
            x1,x2 = np.min(X), np.max(X)
            y1,y2 = np.min(Y), np.max(Y)
            num_pixels = np.sum(mask)
            objs.append(dict(
                mask=resized_mask,
                category=category,
                box=[x1,y1,x2,y2],
                inst_id=inst_id
            ))

        return objs

    def html(self,img_var,output_var,output):
        step_name = html_step_name(self.step_name)
        output_var = html_var_name(output_var)
        img_var = html_var_name(img_var)
        img_arg = html_arg_name('image')
        output = html_embed_image(output,300)
        return f"""<div>{output_var}={step_name}({img_arg}={img_var})={output}</div>"""

    def execute(self,prog_step,inspect=False):
        img_var,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        objs = self.pred_seg(img)
        prog_step.state[output_var] = objs
        if inspect:
            labels = [str(obj['inst_id'])+':'+obj['category'] for obj in objs]
            obj_img = vis_masks(img, objs, labels)
            html_str = self.html(img_var, output_var, obj_img)
            return objs, html_str

        return objs


class SelectInterpreter():
    step_name = 'SELECT'

    def __init__(self):
        print(f'Registering {self.step_name} step')
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.model = CLIPModel.from_pretrained(
            "openai/clip-vit-large-patch14").to(self.device)
        self.model.eval()
        self.processor = CLIPProcessor.from_pretrained(
            "openai/clip-vit-large-patch14")

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        img_var = parse_result['args']['image']
        obj_var = parse_result['args']['object']
        query = eval(parse_result['args']['query']).split(',')
        category = eval(parse_result['args']['category'])
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return img_var,obj_var,query,category,output_var

    def calculate_sim(self,inputs):
        img_feats = self.model.get_image_features(inputs['pixel_values'])
        text_feats = self.model.get_text_features(inputs['input_ids'])
        img_feats = img_feats / img_feats.norm(p=2, dim=-1, keepdim=True)
        text_feats = text_feats / text_feats.norm(p=2, dim=-1, keepdim=True)
        return torch.matmul(img_feats,text_feats.t())

    def query_obj(self,query,objs,img):
        images = [img.crop(obj['box']) for obj in objs]
        text = [f'a photo of {q}' for q in query]
        inputs = self.processor(
            text=text, images=images, return_tensors="pt", padding=True)
        inputs = {k:v.to(self.device) for k,v in inputs.items()}
        with torch.no_grad():
            scores = self.calculate_sim(inputs).cpu().numpy()
            
        obj_ids = scores.argmax(0)
        return [objs[i] for i in obj_ids]

    def html(self,img_var,obj_var,query,category,output_var,output):
        step_name = html_step_name(self.step_name)
        image_arg = html_arg_name('image')
        obj_arg = html_arg_name('object')
        query_arg = html_arg_name('query')
        category_arg = html_arg_name('category')
        image_var = html_var_name(img_var)
        obj_var = html_var_name(obj_var)
        output_var = html_var_name(output_var)
        output = html_embed_image(output,300)
        return f"""<div>{output_var}={step_name}({image_arg}={image_var},{obj_arg}={obj_var},{query_arg}={query},{category_arg}={category})={output}</div>"""

    def query_string_match(self,objs,q):
        obj_cats = [obj['category'] for obj in objs]
        q = q.lower()
        for cat in [q,f'{q}-merged',f'{q}-other-merged']:
            if cat in obj_cats:
                return [obj for obj in objs if obj['category']==cat]
        
        return None

    def execute(self,prog_step,inspect=False):
        img_var,obj_var,query,category,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        objs = prog_step.state[obj_var]
        select_objs = []

        if category is not None:
            cat_objs = [obj for obj in objs if obj['category'] in category]
            if len(cat_objs) > 0:
                objs = cat_objs


        if category is None:
            for q in query:
                matches = self.query_string_match(objs, q)
                if matches is None:
                    continue
                
                select_objs += matches

        if query is not None and len(select_objs)==0:
            select_objs = self.query_obj(query, objs, img)

        prog_step.state[output_var] = select_objs
        if inspect:
            select_obj_img = vis_masks(img, select_objs)
            html_str = self.html(img_var, obj_var, query, category, output_var, select_obj_img)
            return select_objs, html_str

        return select_objs


class ColorpopInterpreter():
    step_name = 'COLORPOP'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        img_var = parse_result['args']['image']
        obj_var = parse_result['args']['object']
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return img_var,obj_var,output_var

    def refine_mask(self,img,mask):
        bgdModel = np.zeros((1,65),np.float64)
        fgdModel = np.zeros((1,65),np.float64)
        mask,_,_ = cv2.grabCut(
            img.astype(np.uint8),
            mask.astype(np.uint8),
            None,
            bgdModel,
            fgdModel,
            5,
            cv2.GC_INIT_WITH_MASK)
        return mask.astype(float)

    def html(self,img_var,obj_var,output_var,output):
        step_name = html_step_name(self.step_name)
        img_var = html_var_name(img_var)
        obj_var = html_var_name(obj_var)
        output_var = html_var_name(output_var)
        img_arg = html_arg_name('image')
        obj_arg = html_arg_name('object')
        output = html_embed_image(output,300)
        return f"""{output_var}={step_name}({img_arg}={img_var},{obj_arg}={obj_var})={output}"""

    def execute(self,prog_step,inspect=False):
        img_var,obj_var,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        objs = prog_step.state[obj_var]
        gimg = img.copy()
        gimg = gimg.convert('L').convert('RGB')
        gimg = np.array(gimg).astype(float)
        img = np.array(img).astype(float)
        for obj in objs:
            refined_mask = self.refine_mask(img, obj['mask'])
            mask = np.tile(refined_mask[:,:,np.newaxis],(1,1,3))
            gimg = mask*img + (1-mask)*gimg

        gimg = np.array(gimg).astype(np.uint8)
        gimg = Image.fromarray(gimg)
        prog_step.state[output_var] = gimg
        if inspect:
            html_str = self.html(img_var, obj_var, output_var, gimg)
            return gimg, html_str

        return gimg


class BgBlurInterpreter():
    step_name = 'BGBLUR'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        img_var = parse_result['args']['image']
        obj_var = parse_result['args']['object']
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return img_var,obj_var,output_var

    def refine_mask(self,img,mask):
        bgdModel = np.zeros((1,65),np.float64)
        fgdModel = np.zeros((1,65),np.float64)
        mask,_,_ = cv2.grabCut(
            img.astype(np.uint8),
            mask.astype(np.uint8),
            None,
            bgdModel,
            fgdModel,
            5,
            cv2.GC_INIT_WITH_MASK)
        return mask.astype(float)

    def smoothen_mask(self,mask):
        mask = Image.fromarray(255*mask.astype(np.uint8)).filter(
            ImageFilter.GaussianBlur(radius = 5))
        return np.array(mask).astype(float)/255

    def html(self,img_var,obj_var,output_var,output):
        step_name = html_step_name(self.step_name)
        img_var = html_var_name(img_var)
        obj_var = html_var_name(obj_var)
        output_var = html_var_name(output_var)
        img_arg = html_arg_name('image')
        obj_arg = html_arg_name('object')
        output = html_embed_image(output,300)
        return f"""{output_var}={step_name}({img_arg}={img_var},{obj_arg}={obj_var})={output}"""

    def execute(self,prog_step,inspect=False):
        img_var,obj_var,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        objs = prog_step.state[obj_var]
        bgimg = img.copy()
        bgimg = bgimg.filter(ImageFilter.GaussianBlur(radius = 2))
        bgimg = np.array(bgimg).astype(float)
        img = np.array(img).astype(float)
        for obj in objs:
            refined_mask = self.refine_mask(img, obj['mask'])
            mask = np.tile(refined_mask[:,:,np.newaxis],(1,1,3))
            mask = self.smoothen_mask(mask)
            bgimg = mask*img + (1-mask)*bgimg

        bgimg = np.array(bgimg).astype(np.uint8)
        bgimg = Image.fromarray(bgimg)
        prog_step.state[output_var] = bgimg
        if inspect:
            html_str = self.html(img_var, obj_var, output_var, bgimg)
            return bgimg, html_str

        return bgimg


class FaceDetInterpreter():
    step_name = 'FACEDET'

    def __init__(self):
        print(f'Registering {self.step_name} step')
        self.model = face_detection.build_detector(
            "DSFDDetector", confidence_threshold=.5, nms_iou_threshold=.3)

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        img_var = parse_result['args']['image']
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return img_var,output_var

    def box_image(self,img,boxes):
        img1 = img.copy()
        draw = ImageDraw.Draw(img1)
        for i,box in enumerate(boxes):
            draw.rectangle(box,outline='blue',width=5)

        return img1

    def enlarge_face(self,box,W,H,f=1.5):
        x1,y1,x2,y2 = box
        w = int((f-1)*(x2-x1)/2)
        h = int((f-1)*(y2-y1)/2)
        x1 = max(0,x1-w)
        y1 = max(0,y1-h)
        x2 = min(W,x2+w)
        y2 = min(H,y2+h)
        return [x1,y1,x2,y2]

    def det_face(self,img):
        with torch.no_grad():
            faces = self.model.detect(np.array(img))
        
        W,H = img.size
        objs = []
        for i,box in enumerate(faces):
            x1,y1,x2,y2,c = [int(v) for v in box.tolist()]
            x1,y1,x2,y2 = self.enlarge_face([x1,y1,x2,y2],W,H)
            mask = np.zeros([H,W]).astype(float)
            mask[y1:y2,x1:x2] = 1.0
            objs.append(dict(
                box=[x1,y1,x2,y2],
                category='face',
                inst_id=i,
                mask = mask
            ))
        return objs

    def html(self,img,output_var,objs):
        step_name = html_step_name(self.step_name)
        box_img = self.box_image(img, [obj['box'] for obj in objs])
        img = html_embed_image(img)
        box_img = html_embed_image(box_img,300)
        output_var = html_var_name(output_var)
        img_arg = html_arg_name('image')
        return f"""<div>{output_var}={step_name}({img_arg}={img})={box_img}</div>"""


    def execute(self,prog_step,inspect=False):
        img_var,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        objs = self.det_face(img)
        prog_step.state[output_var] = objs
        if inspect:
            html_str = self.html(img, output_var, objs)
            return objs, html_str

        return objs


class EmojiInterpreter():
    step_name = 'EMOJI'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        img_var = parse_result['args']['image']
        obj_var = parse_result['args']['object']
        emoji_name = eval(parse_result['args']['emoji'])
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return img_var,obj_var,emoji_name,output_var

    def add_emoji(self,objs,emoji_name,img):
        W,H = img.size
        emojipth = os.path.join(EMOJI_DIR,f'smileys/{emoji_name}.png')
        for obj in objs:
            x1,y1,x2,y2 = obj['box']
            cx = (x1+x2)/2
            cy = (y1+y2)/2
            s = (y2-y1)/1.5
            x_pos = (cx-0.5*s)/W
            y_pos = (cy-0.5*s)/H
            emoji_size = s/H
            emoji_aug = imaugs.OverlayEmoji(
                emoji_path=emojipth,
                emoji_size=emoji_size,
                x_pos=x_pos,
                y_pos=y_pos)
            img = emoji_aug(img)

        return img

    def html(self,img_var,obj_var,emoji_name,output_var,img):
        step_name = html_step_name(self.step_name)
        image_arg = html_arg_name('image')
        obj_arg = html_arg_name('object')
        emoji_arg = html_arg_name('emoji')
        image_var = html_var_name(img_var)
        obj_var = html_var_name(obj_var)
        output_var = html_var_name(output_var)
        img = html_embed_image(img,300)
        return f"""<div>{output_var}={step_name}({image_arg}={image_var},{obj_arg}={obj_var},{emoji_arg}='{emoji_name}')={img}</div>"""

    def execute(self,prog_step,inspect=False):
        img_var,obj_var,emoji_name,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        objs = prog_step.state[obj_var]
        img = self.add_emoji(objs, emoji_name, img)
        prog_step.state[output_var] = img
        if inspect:
            html_str = self.html(img_var, obj_var, emoji_name, output_var, img)
            return img, html_str

        return img


class ListInterpreter():
    step_name = 'LIST'

    prompt_template = """
Create comma separated lists based on the query.

Query: List at most 3 primary colors separated by commas
List:
red, blue, green

Query: List at most 2 north american states separated by commas
List:
California, Washington

Query: List at most {list_max} {text} separated by commas
List:"""

    def __init__(self):
        print(f'Registering {self.step_name} step')
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        text = eval(parse_result['args']['query'])
        list_max = eval(parse_result['args']['max'])
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return text,list_max,output_var

    def get_list(self,text,list_max):
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=self.prompt_template.format(list_max=list_max,text=text),
            temperature=0.7,
            max_tokens=256,
            top_p=0.5,
            frequency_penalty=0,
            presence_penalty=0,
            n=1,
        )

        item_list = response.choices[0]['text'].lstrip('\n').rstrip('\n').split(', ')
        return item_list

    def html(self,text,list_max,item_list,output_var):
        step_name = html_step_name(self.step_name)
        output_var = html_var_name(output_var)
        query_arg = html_arg_name('query')
        max_arg = html_arg_name('max')
        output = html_output(item_list)
        return f"""<div>{output_var}={step_name}({query_arg}='{text}', {max_arg}={list_max})={output}</div>"""

    def execute(self,prog_step,inspect=False):
        text,list_max,output_var = self.parse(prog_step)
        item_list = self.get_list(text,list_max)
        prog_step.state[output_var] = item_list
        if inspect:
            html_str = self.html(text, list_max, item_list, output_var)
            return item_list, html_str

        return item_list


class ClassifyInterpreter():
    step_name = 'CLASSIFY'

    def __init__(self):
        print(f'Registering {self.step_name} step')
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.model = CLIPModel.from_pretrained(
            "openai/clip-vit-large-patch14").to(self.device)
        self.model.eval()
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        image_var = parse_result['args']['image']
        obj_var = parse_result['args']['object']
        category_var = parse_result['args']['categories']
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return image_var,obj_var,category_var,output_var

    def calculate_sim(self,inputs):
        img_feats = self.model.get_image_features(inputs['pixel_values'])
        text_feats = self.model.get_text_features(inputs['input_ids'])
        img_feats = img_feats / img_feats.norm(p=2, dim=-1, keepdim=True)
        text_feats = text_feats / text_feats.norm(p=2, dim=-1, keepdim=True)
        return torch.matmul(img_feats,text_feats.t())

    def query_obj(self,query,objs,img):
        if len(objs)==0:
            images = [img]
            return []
        else:
            images = [img.crop(obj['box']) for obj in objs]

        if len(query)==1:
            query = query + ['other']

        text = [f'a photo of {q}' for q in query]
        inputs = self.processor(
            text=text, images=images, return_tensors="pt", padding=True)
        inputs = {k:v.to(self.device) for k,v in inputs.items()}
        with torch.no_grad():
            sim = self.calculate_sim(inputs)
            

        # if only one query then select the object with the highest score
        if len(query)==1:
            scores = sim.cpu().numpy()
            obj_ids = scores.argmax(0)
            obj = objs[obj_ids[0]]
            obj['class']=query[0]
            obj['class_score'] = 100.0*scores[obj_ids[0],0]
            return [obj]

        # assign the highest scoring class to each object but this may assign same class to multiple objects
        scores = sim.cpu().numpy()
        cat_ids = scores.argmax(1)
        for i,(obj,cat_id) in enumerate(zip(objs,cat_ids)):
            class_name = query[cat_id]
            class_score = scores[i,cat_id]
            obj['class'] = class_name #+ f'({score_str})'
            obj['class_score'] = round(class_score*100,1)

        # sort by class scores and then for each class take the highest scoring object
        objs = sorted(objs,key=lambda x: x['class_score'],reverse=True)
        objs = [obj for obj in objs if 'class' in obj]
        classes = set([obj['class'] for obj in objs])
        new_objs = []
        for class_name in classes:
            cls_objs = [obj for obj in objs if obj['class']==class_name]

            max_score = 0
            max_obj = None
            for obj in cls_objs:
                if obj['class_score'] > max_score:
                    max_obj = obj
                    max_score = obj['class_score']

            new_objs.append(max_obj)

        return new_objs

    def html(self,img_var,obj_var,objs,cat_var,output_var):
        step_name = html_step_name(self.step_name)
        output = []
        for obj in objs:
            output.append(dict(
                box=obj['box'],
                tag=obj['class'],
                score=obj['class_score']
            ))
        output = html_output(output)
        output_var = html_var_name(output_var)
        img_var = html_var_name(img_var)
        cat_var = html_var_name(cat_var)
        obj_var = html_var_name(obj_var)
        img_arg = html_arg_name('image')
        cat_arg = html_arg_name('categories')
        return f"""<div>{output_var}={step_name}({img_arg}={img_var},{cat_arg}={cat_var})={output}</div>"""

    def execute(self,prog_step,inspect=False):
        image_var,obj_var,category_var,output_var = self.parse(prog_step)
        img = prog_step.state[image_var]
        objs = prog_step.state[obj_var]
        cats = prog_step.state[category_var]
        objs = self.query_obj(cats, objs, img)
        prog_step.state[output_var] = objs
        if inspect:
            html_str = self.html(image_var,obj_var,objs,category_var,output_var)
            return objs, html_str

        return objs


class TagInterpreter():
    step_name = 'TAG'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        img_var = parse_result['args']['image']
        obj_var = parse_result['args']['object']
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return img_var,obj_var,output_var

    def tag_image(self,img,objs):
        W,H = img.size
        img1 = img.copy()
        draw = ImageDraw.Draw(img1)
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', 16)
        for i,obj in enumerate(objs):
            box = obj['box']
            draw.rectangle(box,outline='green',width=4)
            x1,y1,x2,y2 = box
            label = obj['class'] + '({})'.format(obj['class_score'])
            if 'class' in obj:
                w,h = font.getsize(label)
                if x1+w > W or y2+h > H:
                    draw.rectangle((x1, y2-h, x1 + w, y2), fill='green')
                    draw.text((x1,y2-h),label,fill='white',font=font)
                else:
                    draw.rectangle((x1, y2, x1 + w, y2 + h), fill='green')
                    draw.text((x1,y2),label,fill='white',font=font)
        return img1

    def html(self,img_var,tagged_img,obj_var,output_var):
        step_name = html_step_name(self.step_name)
        img_var = html_var_name(img_var)
        obj_var = html_var_name(obj_var)
        tagged_img = html_embed_image(tagged_img,300)
        img_arg = html_arg_name('image')
        obj_arg = html_arg_name('objects')
        output_var = html_var_name(output_var)
        return f"""<div>{output_var}={step_name}({img_arg}={img_var}, {obj_arg}={obj_var})={tagged_img}</div>"""

    def execute(self,prog_step,inspect=False):
        img_var,obj_var,output_var = self.parse(prog_step)
        original_img = prog_step.state[img_var]
        objs = prog_step.state[obj_var]
        img = self.tag_image(original_img, objs)
        prog_step.state[output_var] = img
        if inspect:
            html_str = self.html(img_var, img, obj_var, output_var)
            return img, html_str

        return img


def dummy(images, **kwargs):
    return images, False

class ReplaceInterpreter():
    step_name = 'REPLACE'

    def __init__(self):
        print(f'Registering {self.step_name} step')
        device = "cuda"
        model_name = "runwayml/stable-diffusion-inpainting"
        self.pipe = StableDiffusionInpaintPipeline.from_pretrained(
            model_name,
            revision="fp16",
            torch_dtype=torch.float16)
        self.pipe = self.pipe.to(device)
        self.pipe.safety_checker = dummy

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        img_var = parse_result['args']['image']
        obj_var = parse_result['args']['object']
        prompt = eval(parse_result['args']['prompt'])
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return img_var,obj_var,prompt,output_var

    def create_mask_img(self,objs):
        mask = objs[0]['mask']
        mask[mask>0.5] = 255
        mask[mask<=0.5] = 0
        mask = mask.astype(np.uint8)
        return Image.fromarray(mask)

    def merge_images(self,old_img,new_img,mask):
        print(mask.size,old_img.size,new_img.size)

        mask = np.array(mask).astype(np.float)/255
        mask = np.tile(mask[:,:,np.newaxis],(1,1,3))
        img = mask*np.array(new_img) + (1-mask)*np.array(old_img)
        return Image.fromarray(img.astype(np.uint8))

    def resize_and_pad(self,img,size=(512,512)):
        new_img = Image.new(img.mode,size)
        thumbnail = img.copy()
        thumbnail.thumbnail(size)
        new_img.paste(thumbnail,(0,0))
        W,H = thumbnail.size
        return new_img, W, H

    def predict(self,img,mask,prompt):
        mask,_,_ = self.resize_and_pad(mask)
        init_img,W,H = self.resize_and_pad(img)
        new_img = self.pipe(
            prompt=prompt,
            image=init_img,
            mask_image=mask,
            # strength=0.98,
            guidance_scale=7.5,
            num_inference_steps=50 #200
        ).images[0]
        return new_img.crop((0,0,W-1,H-1)).resize(img.size)

    def html(self,img_var,obj_var,prompt,output_var,output):
        step_name = html_step_name(img_var)
        img_var = html_var_name(img_var)
        obj_var = html_var_name(obj_var)
        output_var = html_var_name(output_var)
        img_arg = html_arg_name('image')
        obj_arg = html_arg_name('object')
        prompt_arg = html_arg_name('prompt')
        output = html_embed_image(output,300)
        return f"""{output_var}={step_name}({img_arg}={img_var},{obj_arg}={obj_var},{prompt_arg}='{prompt}')={output}"""

    def execute(self,prog_step,inspect=False):
        img_var,obj_var,prompt,output_var = self.parse(prog_step)
        img = prog_step.state[img_var]
        objs = prog_step.state[obj_var]
        mask = self.create_mask_img(objs)
        new_img = self.predict(img, mask, prompt)
        prog_step.state[output_var] = new_img
        if inspect:
            html_str = self.html(img_var, obj_var, prompt, output_var, new_img)
            return new_img, html_str
        return new_img


def register_step_interpreters(dataset='nlvr'):
    if dataset=='nlvr':
        return dict(
            VQA=VQAInterpreter(),
            EVAL=EvalInterpreter(),
            RESULT=ResultInterpreter(),
            CAP=CapInterpreter()
        )
    elif dataset=='gqa':
        return dict(
            LOC=LocInterpreter(),
            COUNT=CountInterpreter(),
            CROP=CropInterpreter(),
            CROP_RIGHTOF=CropRightOfInterpreter(),
            CROP_LEFTOF=CropLeftOfInterpreter(),
            CROP_FRONTOF=CropFrontOfInterpreter(),
            CROP_INFRONTOF=CropInFrontOfInterpreter(),
            CROP_INFRONT=CropInFrontInterpreter(),
            CROP_BEHIND=CropBehindInterpreter(),
            CROP_AHEAD=CropAheadInterpreter(),
            CROP_BELOW=CropBelowInterpreter(),
            CROP_ABOVE=CropAboveInterpreter(),
            VQA=VQAInterpreter(),
            EVAL=EvalInterpreter(),
            RESULT=ResultInterpreter(),
            CAP=CapInterpreter(),
            GET=GetInterpreter(),
            GET_TOP=GetTopInterpreter(),
            GET_BOTTOM=GetBottomInterpreter(),
            GET_LEFT=GetLeftInterpreter(),
            GET_RIGHT=GetRightInterpreter()
        )
    elif dataset=='imageEdit':
        return dict(
            FACEDET=FaceDetInterpreter(),
            SEG=SegmentInterpreter(),
            SELECT=SelectInterpreter(),
            COLORPOP=ColorpopInterpreter(),
            BGBLUR=BgBlurInterpreter(),
            REPLACE=ReplaceInterpreter(),
            EMOJI=EmojiInterpreter(),
            RESULT=ResultInterpreter()
        )
    elif dataset=='okDet':
        return dict(
            FACEDET=FaceDetInterpreter(),
            LIST=ListInterpreter(),
            CLASSIFY=ClassifyInterpreter(),
            RESULT=ResultInterpreter(),
            TAG=TagInterpreter(),
            LOC=Loc2Interpreter(thresh=0.05,nms_thresh=0.3)
        )