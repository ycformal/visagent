import os
import json
import io, tokenize

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

# read all files in the directory
def read_files(directory):
    files = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            filename = file.split(".")[0]
            if filename != 'sys':
                files.append(filename)
    return files

# read the system file and store the text into a string. Turn '"' to be '\"'.
def read_sys_file(directory):
    sys_file = 'sys.txt'
    sys_file_path = os.path.join(directory, sys_file)
    with open(sys_file_path, 'r') as f:
        sys_text = f.read()
    return sys_text

def longest_common_prefix(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]

sys_text = read_sys_file('./')

dataset = []
files = read_files('./')
files=[str(i) for i in range(1, 60)]

for file in files:
    file_path = os.path.join('./', file + '.txt')
    with open(file_path, 'r') as f:
        text = f.read()
    context = text.split('<End of Context>')[0] + '<End of Context>'
    steps = text.split('<End of Context>')[1]
    steps = steps.split('<End of Plan>')[0]
    steps = steps.strip()
    steps = steps.split('\n')
    next_line = 0
    while next_line < len(steps):
        current_context = context
        if next_line > 0:
            current_context += '\n\n'
            current_context += '\n'.join(steps[:next_line]) + '\n'
            current_context += '\n<End of Plan>'
        thought = steps[next_line] + '\n'
        next_line += 1
        implement = steps[next_line] + '\n'
        next_line += 1
        response = thought + implement
        if 'Thought(' not in thought[:8] or ')' != thought[-2] or 'Implement(' not in implement[:10] or ')' != implement[-2]:
            print(thought)
            print(implement)
            print(response)
            raise Exception(f'{file}.txt: Thought or Implement is not in the correct format')
        statement = implement[10:-2]
        try:
            parsed_step = parse_step(statement)
            if parsed_step['step_name'] not in ['VQA', 'LOC', 'CROP', 'COUNT', 'CROP_LEFTOF', 'CROP_RIGHTOF', 'CROP_ABOVE', 'CROP_BELOW', 'FILTER_INCLUDED', 'RESULT', 'EVAL']:
                print(statement, parsed_step['step_name'])
        except:
            print(statement)
            raise Exception(f'{file}.txt: Implement is not in the correct format')
        # assert statement is of format variavle=function(arg1=arg1,arg2=arg2,...)
        if '=' not in statement or '(' not in statement.split('=')[1] or ')' != statement[-1]:
            raise Exception(f'{file}.txt: Implement is not in the correct format')
        dataset.append({"messages": [{"role": "system", "content": sys_text}, {"role": "user", "content": current_context}, {"role": "assistant", "content": response}]})
        while next_line < len(steps) and '</result>' not in steps[next_line]:
            if 'Thought(' in steps[next_line]:
                raise Exception(f'{file}.txt: <result> is not closed')
            next_line += 1
        next_line += 1

# write the dataset into a json file
with open('dataset.jsonl', 'w') as f:
    for data in dataset:
        # Convert the dictionary to a JSON string with double quotes
        json_string = json.dumps(data)  # `json.dumps` ensures double quotes are used
        f.write(json_string + '\n')
