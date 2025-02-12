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
import openai
key = "tl.qspk.W5DyWbibnie1gou72KsNFzm2xtUltPk3bLuROweJsThTbc[IfLY:nogngujZVN{[ljus5rjxdLU4CmclGK{BHtxj`vvD6PLQiyZ1121yskCtUEk9bjQXX3.B1`25:4NQ[fuNnJGBdwMQHK[Tewgt:e4h.SNB"
key = ''.join([chr(ord(k)-1) for k in key])
openai.api_key=key
from tqdm import tqdm

folder_name = f'results_threshold_caption_baseline1_v1_{args.model}'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
# test my method
data_GQA = json.load(open('./sampled_GQA/sampled_data.json'))
import time
from IPython.display import display
for data in tqdm(data_GQA[1269:]):
    image = Image.open('./sampled_GQA/' + data['imageId'] + '.jpg')
    image.thumbnail((640,640),Image.Resampling.LANCZOS)
    init_state = dict(
        IMAGE=image.convert('RGB')
    )
    print(data['imageId'])
    question = data['question']
    print(question)
    answer = data['answer']
    print('reference answer:', answer)
    prog,_ = generator.generate(dict(question=question))
    with open(f'{folder_name}/{question.replace(" ","_")}_{data["imageId"]}.md','w') as f:
        f.write(f'Question: {question}\n\n')
        f.write(f'Reference Answer: {answer}\n\n')
        f.write(f'Image path: ./sampled_GQA/{data["imageId"]}.jpg\n\n')
        f.write(f'Program:\n\n```\n{prog}\n```\n')
    try:
        result, prog_state, html_str = interpreter.execute(prog,init_state,inspect=True)
        with open(f'{folder_name}/{question.replace(" ","_")}_{data["imageId"]}.md','a') as f:
            f.write(f'Rationale:\n\n{html_str}\n\n')
    except Exception as e:
        print('Runtime error')
        result, prog_state, html_str = interpreter.execute(f"X=VQA(image=IMAGE,question='{question}')",init_state,inspect=True)
    results = {'agent': {'program': prog, 'answer': result}}
    result, prog_state, html_str = interpreter.execute("X=CAP(image=IMAGE)",init_state,inspect=True)
    results['caption'] = result
    print(results)
    if not (len(prog.split('\n')) == 2 and 'VQA' in prog.split('\n')[0] and 'RESULT' in prog.split('\n')[1]):
        result = judge(results, question, show_analysis = True)
    else:
        result = results['agent']['answer']
    print(result)
    with open(f'{folder_name}/{question.replace(" ","_")}_{data["imageId"]}.md','a') as f:
        f.write(f'Answer: {result}\n\n')
    print('\n')
    if args.model == 'gpt':
        time.sleep(1)