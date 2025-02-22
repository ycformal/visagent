# from .step_interpreters import parse_step

import nltk
nltk.download('averaged_perceptron_tagger_eng')
import inflect
import io
import tokenize

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

def validate(program, question, module_list, state_dict = {"IMAGE": None}):
    inflect_engine = inflect.engine()
    lines =program.split('\n')
    for i, line in enumerate(program.split('\n')):
        parse_result = parse_step(line)
        step_name = parse_result['step_name']
        output_var = parse_result['output_var']
        if step_name not in module_list:
            # print(f"Invalid step name: {step_name}")
            return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
        if step_name == "EVAL":
            try:
                expr = eval(parse_result['args']['expr'])
                for var_name,var_value in state_dict.items():
                    if isinstance(var_value,str):
                        if var_value in ['yes','no']:
                            state_dict[var_name] = var_value=='yes'
                        elif var_value.isdecimal():
                            state_dict[var_name] = var_value
                        else:
                            state_dict[var_name] = f"'{var_value}'"
                    else:
                        state_dict[var_name] = var_value

                if 'xor' in expr:
                    expr = expr.replace('xor','!=')

                expr = expr.format(**state_dict)
                step_output = eval(expr)
                state_dict[output_var] = step_output

                lines[i] = line.replace(" == 'no'", " == False")
                lines[i] = lines[i].replace(" == 'yes'", " == True")
            except:
                # print(f"Invalid expression: {parse_result['args']['expr']}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
        elif step_name == "LOC":
            object_name = eval(parse_result['args']['object'])
            last_word =object_name.split()[-1]
            output_var = parse_result['output_var']
            # judge whether the last word is a noun
            if nltk.pos_tag([last_word])[0][1] not in ['NN','NNS','NNP','NNPS']:
                # print(f"Invalid object name: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            image = parse_result['args']['image']
            if image not in state_dict:
                # print(f"Invalid image: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            if nltk.pos_tag([last_word])[0][1] in ['NNS','NNPS']:
                lines[i] = f"{output_var}=LOC(image={image},object='{object_name}',plural=True)"
            last_word_plural = inflect_engine.plural(last_word)
            question_clean = question.replace('?','')
            question_clean = question_clean.replace('.','')
            question_clean = question_clean.replace(',','')
            if last_word not in question_clean.split() and last_word_plural not in question_clean.split():
                # print(f"Invalid object: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            if last_word not in question_clean.split() and last_word_plural in question_clean.split():
                lines[i] = f"{output_var}=LOC(image={image},object='{object_name}',plural=True)"
            state_dict[output_var] = [[0,0,100,100]]
        elif 'CROP' in step_name:
            box = parse_result['args']['box']
            image = parse_result['args']['image']
            if image not in state_dict or box not in state_dict:
                # print(f"Invalid image or box: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            output_var = parse_result['output_var']
            state_dict[output_var] = state_dict[image]
        elif step_name == "COUNT":
            box = parse_result['args']['box']
            if box not in state_dict:
                # print(f"Invalid box: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            output_var = parse_result['output_var']
            state_dict[output_var] = len(state_dict[box])
        elif step_name == "VQA":
            image = parse_result['args']['image']
            if image not in state_dict:
                # print(f"Invalid image: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            output_var = parse_result['output_var']
            state_dict[output_var] = '0'
        elif step_name == "RESULT":
            var = parse_result['args']['var']
            if var not in state_dict:
                # print(f"Invalid var: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            output_var = parse_result['output_var']
            state_dict[output_var] = state_dict[var]
        elif step_name == "GET":
            image = parse_result['args']['image']
            if image not in state_dict:
                # print(f"Invalid image: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            output_var = parse_result['output_var']
            state_dict[output_var] = state_dict[image]
        else:
            # print(f"Invalid step name: {step_name}")
            return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
    program = '\n'.join(lines)
    return program
