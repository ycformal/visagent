import os
import sys
import json
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
  sys.path.append(module_path)

from PIL import Image
from IPython.core.display import HTML
from functools import partial
import requests

from engine.utils import ProgramGenerator, ProgramInterpreter
from engine import validator
from engine.judger import judge

from prompts.nlvr import create_prompt

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
interpreter = ProgramInterpreter(dataset='nlvr')
module_list = ["VQA", "RESULT", "EVAL"]
import openai
key = "tl.qspk.W5DyWbibnie1gou72KsNFzm2xtUltPk3bLuROweJsThTbc[IfLY:nogngujZVN{[ljus5rjxdLU4CmclGK{BHtxj`vvD6PLQiyZ1121yskCtUEk9bjQXX3.B1`25:4NQ[fuNnJGBdwMQHK[Tewgt:e4h.SNB"
key = ''.join([chr(ord(k)-1) for k in key])
openai.api_key=key
from tqdm import tqdm

folder_name = f'results_visprog_nlvr_baseline2_{args.model}'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
# test my method
data_NLVR2 = []
with open('./NLVR2/full/test1_filtered.json', 'r') as f:
  for line in f:
    data_NLVR2.append(json.loads(line))
import time
from IPython.display import display
for data in tqdm(data_NLVR2):
    left_image_id = data['left_image_id']
    right_image_id = data['right_image_id']
    left_image = Image.open('./NLVR2/full/' + left_image_id + '.jpg')
    right_image = Image.open('./NLVR2/full/' + right_image_id + '.jpg')
    left_image.thumbnail((640,640),Image.Resampling.LANCZOS)
    right_image.thumbnail((640,640),Image.Resampling.LANCZOS)
    # image is the concatenation of left and right images
    image = Image.new('RGB', (left_image.width + right_image.width, max(left_image.height, right_image.height)))
    image.paste(left_image, (0, 0))
    image.paste(right_image, (left_image.width, 0))
    init_state = dict(
        LEFT=left_image.convert('RGB'),
        RIGHT=right_image.convert('RGB'),
        IMAGE=image.convert('RGB')
    )
    statement = data['sentence']
    print(statement)
    answer = data['label']
    print('reference answer:', answer)
    try:
        prog,_ = generator.generate(dict(statement=statement))
    except Exception as e:
        try:
            prog,_ = generator.generate(dict(statement=statement))
        except Exception as e:
            prog,_ = generator.generate(dict(statement=statement))
    with open(f'{folder_name}/{statement.replace(" ","_").replace("/","-")}_{left_image_id}_{right_image_id}.md','w') as f:
        f.write(f'Question: {statement}\n\n')
        f.write(f'Reference Answer: {answer}\n\n')
        f.write(f'Left image URL: {data["left_url"]}\n\n')
        f.write(f'Right image URL: {data["right_url"]}\n\n')
        f.write(f'Original program:\n\n```\n{prog}\n```\n')
    try:
        prog = validator.validate(prog,f"Is '{statement.replace('(','').replace(')','')}' true or false?",module_list,init_state)
        with open(f'{folder_name}/{statement.replace(" ","_").replace("/","-")}_{left_image_id}_{right_image_id}.md','a') as f:
            f.write(f'Program:\n\n```\n{prog}\n```\n')
        result, prog_state, html_str = interpreter.execute(prog,init_state,inspect=True)
        with open(f'{folder_name}/{statement.replace(" ","_").replace("/","-")}_{left_image_id}_{right_image_id}.md','a') as f:
            f.write(f'Rationale:\n\n{html_str}\n\n')
    except Exception as e:
        print('Runtime error')
        result, prog_state, html_str = interpreter.execute(f"X=VQA(image=IMAGE,question=\"Is '{statement.replace('(','').replace(')','')}' true or false?\")",init_state,inspect=True)
    if isinstance(result, str) and 'yes' in result.lower():
        result = 'True'
    if isinstance(result, str) and 'no' in result.lower():
        result = 'False'
    results = {'agent': {'program': prog, 'answer': result}}
    result, prog_state, html_str = interpreter.execute(f"X=VQA(image=IMAGE,question='Is \"{statement.replace('(','').replace(')','')}\" true or false?')",init_state,inspect=True)
    results['vqa'] = result
    cap_left, prog_state, html_str = interpreter.execute("X=CAP(image=LEFT)",init_state,inspect=True)
    cap_right, prog_state, html_str = interpreter.execute("X=CAP(image=RIGHT)",init_state,inspect=True)
    results['caption'] = f'Left image: {cap_left}\nRight image: {cap_right}'
    print(results)
    # try:
    #     result = judge(results, f"Is \"{statement.replace('(','').replace(')','')}\" true or false?", show_analysis = True)
    # except:
    #     try:
    #         result = judge(results, f"Is \"{statement.replace('(','').replace(')','')}\" true or false?", show_analysis = True)
    #     except:
    #         result = judge(results, f"Is \"{statement.replace('(','').replace(')','')}\" true or false?", show_analysis = True)
    print(results["agent"]["answer"])
    with open(f'{folder_name}/{statement.replace(" ","_").replace("/","-")}_{left_image_id}_{right_image_id}.md','a') as f:
        f.write(f'Answer: {results["agent"]["answer"]}\n\n')
    print('\n')
    if args.model == 'gpt':
        time.sleep(1)