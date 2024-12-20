import os
from PIL import Image
import openai
import numpy as np
import copy

from .step_interpreters import register_step_interpreters, parse_step


class Program:
    def __init__(self,prog_str,init_state=None):
        self.prog_str = prog_str
        self.state = init_state if init_state is not None else dict()
        self.instructions = self.prog_str.split('\n')


class ProgramInterpreter:
    def __init__(self,dataset='nlvr'):
        self.step_interpreters = register_step_interpreters(dataset)

    def execute_step(self,prog_step,inspect):
        step_name = parse_step(prog_step.prog_str,partial=True)['step_name']
        print(step_name)
        return self.step_interpreters[step_name].execute(prog_step,inspect)

    def execute(self,prog,init_state,inspect=False):
        results = []
        if isinstance(prog,str):
            prog = Program(prog,init_state)
        else:
            assert(isinstance(prog,Program))

        prog_steps = [Program(instruction,init_state=prog.state) \
            for instruction in prog.instructions]

        html_str = '<hr>'
        for prog_step in prog_steps:
            if inspect:
                step_output, step_html = self.execute_step(prog_step,inspect)
                html_str += step_html + '<hr>'
            else:
                step_output = self.execute_step(prog_step,inspect)
            results.append(step_output)

        if inspect:
            return step_output, prog.state, html_str, results

        return step_output, prog.state, results


class ProgramGenerator():
    def __init__(self,prompter,temperature=0.7,top_p=0.5,prob_agg='mean',in_context_learning = True):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.prompter = prompter
        self.temperature = temperature
        self.top_p = top_p
        self.prob_agg = prob_agg
        self.in_context_learning = in_context_learning

    def compute_prob(self,response):
        eos = '<|endoftext|>'
        for i,token in enumerate(response.choices[0]['logprobs']['tokens']):
            if token==eos:
                break

        if self.prob_agg=='mean':
            agg_fn = np.mean
        elif self.prob_agg=='sum':
            agg_fn = np.sum
        else:
            raise NotImplementedError

        return np.exp(agg_fn(
            response.choices[0]['logprobs']['token_logprobs'][:i]))

    def generate(self,inputs):
        if self.in_context_learning:
            response = openai.Completion.create(
                model="gpt-3.5-turbo-instruct",
                prompt=self.prompter(inputs),
                temperature=self.temperature,
                max_tokens=512,
                top_p=self.top_p,
                frequency_penalty=0,
                presence_penalty=0,
                n=1,
                # stop = ')\n',
                logprobs=1
            )

            prob = self.compute_prob(response)
            prog = response.choices[0]['text'].lstrip('\n').rstrip('\n')
            return prog, prob, self.prompter(inputs)
        else:
            system_inst = None
            with open('dataset_revised/sys.txt', 'r') as fp:
                system_inst = fp.read()
            response = openai.ChatCompletion.create(
                model="ft:gpt-3.5-turbo-1106:personal:trial1030:AO4vADm5",
                messages=[
                    {
                        "role": "system",
                        "content": f"{system_inst}"
                    },
                    {
                        "role": "user",
                        "content": f"{inputs['input']}"
                    }
                ],
                temperature = self.temperature,
                n=1,
                top_p=self.top_p,
                frequency_penalty=0,
                presence_penalty=0
              )
            return response['choices'][0]['message']['content'].strip(), 1.0
    
