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
# from engine.judger import judge
# from engine.converter import convert
from prompts.gqa_old import create_prompt
prompter = partial(create_prompt,method='all')
generator = ProgramGenerator(prompter=prompter)
interpreter = ProgramInterpreter(dataset='gqa')
import openai
openai.api_key="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"
from tqdm import tqdm

folder_name = 'results_visprog_mixtral'
# test my method
data_GQA = json.load(open('./sampled_GQA/sampled_data.json'))
import time
from IPython.display import display
for data in tqdm(data_GQA):
    image = Image.open('./sampled_GQA/' + data['imageId'] + '.jpg')
    image.thumbnail((640,640),Image.Resampling.LANCZOS)
    init_state = dict(
        IMAGE=image.convert('RGB')
    )
    question = data['question']
    print(question)
    answer = data['answer']
    print('reference answer:', answer)
    prog,_,_ = generator.generate(dict(question=question))
    with open(f'{folder_name}/{question.replace(" ","_")}_{data["imageId"]}.md','w') as f:
        f.write(f'Question: {question}\n\n')
        f.write(f'Reference Answer: {answer}\n\n')
        f.write(f'Image path: ./sampled_GQA/{data["imageId"]}.jpg\n\n')
        f.write(f'Program:\n\n```\n{prog}\n```\n')
    try:
        result, prog_state, html_str = interpreter.execute(prog,init_state,inspect=True)
        with open(f'{folder_name}/{question.replace(" ","_")}_{data["imageId"]}.md','a') as f:
            f.write(f'Rationale:\n\n{html_str}\n\n')
        # print(result)
    except Exception as e:
        result = 'Runtime error: ' + str(e)
    results = {'agent': {'program': prog, 'answer': result}}
    result, prog_state, html_str = interpreter.execute(f"X=VQA(image=IMAGE,question='{question}')",init_state,inspect=True)
    results['vqa'] = result
    result, prog_state, html_str = interpreter.execute("X=CAP(image=IMAGE)",init_state,inspect=True)
    results['caption'] = result
    print(results)
    with open(f'{folder_name}/{question.replace(" ","_")}_{data["imageId"]}.md','a') as f:
        f.write(f'Answer: {results["agent"]["answer"]}\n\n')
    print('\n')