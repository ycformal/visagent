import os
import sys
import json
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
  sys.path.append(module_path)

from PIL import Image
from IPython.core.display import HTML
from functools import partial

from engine.utils import ProgramGenerator, ProgramInterpreter
from engine.judger import judge
from engine import validator
from prompts.gqa_baseline1_v1 import create_prompt
import argparse

parser = argparse.ArgumentParser(description='Run the threshold captioning experiment')
parser.add_argument('--model', type=str, default='gpt', help='Model to generate the script')
args = parser.parse_args()

model = None
if args.model == 'gpt':
    model = 'gpt-3.5-turbo-instruct'
elif args.model == 'llama':
    model = 'meta-llama/Meta-Llama-3-8B'
elif args.model == 'glm':
    model = 'THUDM/glm-4-9b-hf'
elif args.model == 'mistral':
    model = 'mistralai/Mistral-Small-24B-Base-2501'
else:
    raise ValueError('Invalid model name')

prompter = partial(create_prompt,method='all')
generator = ProgramGenerator(prompter=prompter, model_name_or_path=model)
interpreter = ProgramInterpreter(dataset='gqa')
module_list = ["LOC", "CROP", "CROP_ABOVE", "CROP_BELOW", "CROP_LEFTOF", "CROP_RIGHTOF", "CROP_BEHIND", "CROP_INFRONT", "CROP_INFRONTOF", "CROP_AHEAD", "FROP_FRONTOF", "COUNT", "VQA", "RESULT", "EVAL", "GET"]
import openai
key = "tl.qspk.W5DyWbibnie1gou72KsNFzm2xtUltPk3bLuROweJsThTbc[IfLY:nogngujZVN{[ljus5rjxdLU4CmclGK{BHtxj`vvD6PLQiyZ1121yskCtUEk9bjQXX3.B1`25:4NQ[fuNnJGBdwMQHK[Tewgt:e4h.SNB"
key = ''.join([chr(ord(k)-1) for k in key])
openai.api_key=key
from tqdm import tqdm

folder_name = f'results_vqav2_baseline2_{args.model}'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
# test my method
data_GQA = json.load(open('./VQAv2/sampled_questions.json'))
import time
from IPython.display import display
for data in tqdm(data_GQA):
    image = Image.open('./VQAv2/images/COCO_val2014_' + str(data['image_id']).zfill(12) + '.jpg')
    image.thumbnail((640,640),Image.Resampling.LANCZOS)
    init_state = dict(
        IMAGE=image.convert('RGB')
    )
    print(data['image_id'])
    question = data['question']
    print(question)
    answer = data['answer']
    print('reference answer:', answer)
    try:
        prog,_ = generator.generate(dict(question=question))
    except Exception as e:
        try:
            prog,_ = generator.generate(dict(question=question))
        except Exception as e:
            prog,_ = generator.generate(dict(question=question))
    with open(f'{folder_name}/{question.replace(" ","_")}_{data["image_id"]}.md','w') as f:
        f.write(f'Question: {question}\n\n')
        f.write(f'Reference Answer: {answer}\n\n')
        f.write(f'Image path: ./sampled_GQA/{data["image_id"]}.jpg\n\n')
        f.write(f'Original program:\n\n```\n{prog}\n```\n')
    try:
        prog = validator.validate(prog,question,module_list)
        with open(f'{folder_name}/{question.replace(" ","_")}_{data["image_id"]}.md','a') as f:
            f.write(f'Program:\n\n```\n{prog}\n```\n')
        result, prog_state, html_str = interpreter.execute(prog,init_state,inspect=True)
        with open(f'{folder_name}/{question.replace(" ","_")}_{data["image_id"]}.md','a') as f:
            f.write(f'Rationale:\n\n{html_str}\n\n')
    except Exception as e:
        print('Runtime error')
        result, prog_state, html_str = interpreter.execute(f"X=VQA(image=IMAGE,question='{question}')",init_state,inspect=True)
    results = {'agent': {'program': prog, 'answer': result}}
    result, prog_state, html_str = interpreter.execute("X=CAP(image=IMAGE)",init_state,inspect=True)
    results['caption'] = result
    print(results)
    try:
        result = judge(results, question, show_analysis = True)
    except:
        try:
            result = judge(results, question, show_analysis = True)
        except:
            result = judge(results, question, show_analysis = True)
    print(result)
    with open(f'{folder_name}/{question.replace(" ","_")}_{data["image_id"]}.md','a') as f:
        f.write(f'Answer: {result}\n\n')
    print('\n')
    if args.model == 'gpt':
        time.sleep(1)