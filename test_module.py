from transformers import (ViltProcessor, ViltForQuestionAnswering, 
    OwlViTProcessor, OwlViTForObjectDetection,
    MaskFormerFeatureExtractor, MaskFormerForInstanceSegmentation,
    CLIPProcessor, CLIPModel, AutoProcessor, BlipForQuestionAnswering, AutoModelForCausalLM)
import torch
import PIL
import os

os.environ['HF_HOME'] = '/home/hice1/yxu846/scratch/models'

img = PIL.Image.open('sampled_GQA/2335971.jpg')

device = "cuda:0" if torch.cuda.is_available() else "cpu"
processor = AutoProcessor.from_pretrained("Salesforce/blip-vqa-capfilt-large")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-capfilt-large").to(device)
model.eval()
encoding = processor(img,"Is the bear wearing white glasses or black glasses?",return_tensors='pt')
encoding = {k:v.to(device) for k,v in encoding.items()}
# print(encoding)
with torch.no_grad():
    outputs = model.generate(**encoding)
# print(outputs)
result = processor.decode(outputs[0], skip_special_tokens=True)
print(result)


# device = "cuda:0" if torch.cuda.is_available() else "cpu"
# processor = OwlViTProcessor.from_pretrained("google/owlvit-large-patch14")
# model = OwlViTForObjectDetection.from_pretrained("google/owlvit-large-patch14").to(device)
# model.eval()
# encoding = processor(
#     text=[[f'a photo of teddy bear']], 
#     images=img,
#     return_tensors='pt')
# # print(encoding)
# encoding = {k:v.to(device) for k,v in encoding.items()}
# with torch.no_grad():
#     outputs = model(**encoding)
#     for k,v in outputs.items():
#         if v is not None:
#             outputs[k] = v.to('cpu') if isinstance(v, torch.Tensor) else v

# # print(outputs)
# target_sizes = torch.Tensor([img.size[::-1]])
# results = processor.post_process_object_detection(outputs=outputs,threshold=0.1,target_sizes=target_sizes)
# boxes, scores = results[0]["boxes"], results[0]["scores"]
# boxes = boxes.cpu().detach().numpy().tolist()
# scores = scores.cpu().detach().numpy().tolist()
# print(results)

# def box_image(img,boxes,highlight_best=True):
#     img1 = img.copy()
#     draw = PIL.ImageDraw.Draw(img1)
#     for i,box in enumerate(boxes):
#         if i==0 and highlight_best:
#             color = 'red'
#         else:
#             color = 'blue'

#         draw.rectangle(box,outline=color,width=5)

#     return img1

# marked = box_image(img,boxes)
# # save the marked image
# marked.save('marked.jpg')