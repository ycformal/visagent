import os
import sys
import json
import io, tokenize
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

import openai
openai.api_key = "*"
import random

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

def analyze(question, caption, size):
    messages = []

    with open('prompts/head.txt', 'r') as f:
        head = f.read()

    with open('prompts/LOC.txt', 'r') as f:
        LOC = f.read()

    with open('prompts/CROP.txt', 'r') as f:
        CROP = f.read()

    with open('prompts/CROP_.txt', 'r') as f:
        CROP_ = f.read()

    with open('prompts/EVAL.txt', 'r') as f:
        EVAL = f.read()

    with open('prompts/VQA.txt', 'r') as f:
        VQA = f.read()

    head = head.format(question=question, caption=caption, size=size)

    messages.append({"role": "user", "content": head})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    response = response['choices'][0]['message']['content']
    while True:
        messages.append({"role": "assistant", "content": response})
        print(response)
        statement = input("Enter the corresponding statement: ")
        new_var = parse_step(statement)['output_var']
        step_name = parse_step(statement)['step_name']
        result = input('Enter the result: ')
        if step_name == 'LOC':
            template = LOC.format(new_var=new_var, result=result, statement=statement)
            messages.append({"role": "user", "content": template})
        elif step_name == 'CROP':
            template = CROP.format(new_var=new_var, result=result, statement=statement)
            messages.append({"role": "user", "content": template})
        elif 'CROP_' in step_name:
            template = CROP_.format(new_var=new_var, result=result, statement=statement)
            messages.append({"role": "user", "content": template})
        elif step_name == 'EVAL':
            template = EVAL.format(new_var=new_var, result=result, statement=statement)
            messages.append({"role": "user", "content": template})
        elif step_name == 'VQA':
            template = VQA.format(new_var=new_var, result=result, statement=statement)
            messages.append({"role": "user", "content": template})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        response = response['choices'][0]['message']['content']

question = "Which kind of furniture hangs from the wall?"
caption = "The image shows a modern kitchen with white cabinets and stainless steel appliances. The kitchen has a large island with a granite countertop and a sink. On the left side of the island, there is a stainless steel refrigerator and a double oven. Above the stove, there are two built-in microwave ovens and a coffee maker. The cabinets are white and the countertop is made of granite. There is a window above the sink with white blinds. The floor is tiled in a light beige color and the walls are painted a light brown color. There are a few items on the countertops, including a toaster, a coffee machine, and a few bags of bread. The overall style of the kitchen is clean and minimalistic."
size = "640wx480h"

analyze(question, caption, size)