import os
import sys
import json
import io, tokenize
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

import openai
openai.api_key = ""
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

def analyze(inputs):
    with open('prompts/template.txt', 'r') as f:
        template = f.read()

    template = template.format(**inputs)
    with open('prompts/formatizer.txt', 'r') as f:
        formatizer = f.read()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "user",
            "content": template
            }
        ]
    )
    response = response['choices'][0]['message']['content']
    formatizer_input = {
        "response": response,
        "question": inputs['question']
    }
    formatizer = formatizer.format(**formatizer_input)
    formatized = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "user",
            "content": formatizer
            }
        ]
    )
    formatized = formatized['choices'][0]['message']['content']
    print(response, formatized)

inputs = {
    "question": "Is there a teddy bear that is not lying?",
    "variables": """IMAGE=<Image, caption="The image shows a teddy bear sitting on the steering wheel of a vintage car. The bear is wearing a black leather jacket with a red scarf around its neck and a pair of black goggles on its head. The car appears to be in motion, as the background is blurred, suggesting that the focus is on the bear and the car.\"""",
    "actions": """none"""
}
analyze(inputs)