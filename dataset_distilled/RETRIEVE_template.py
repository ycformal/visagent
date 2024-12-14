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

template = ''
files = read_files('./')
files=[str(i) for i in range(1, 61)]

for file in files:
    file_path = os.path.join('./', file + '.txt')
    with open(file_path, 'r') as f:
        text = f.read()
    question = '"'.join(text.split('<End of Context>')[0].split('Q="')[1].split('"')[:-1]).strip()
    template += 'question: ' + question + '\n'
    statements = text.split('</result>')
    for statement in statements:
        if 'CAP0=CAP(image=IMAGE)' in statement:
            result = statement.split('<result>')[1].strip()
            template += 'caption: ' + result + '\n'
        elif 'X=RETRIEVE(question=Q,caption=CAP0)' in statement:
            result = statement.split('<result>')[1].strip()
            template += 'response: ' + result + '\n'

# write the dataset into a json file
with open('retrieve_template.txt', 'w') as f:
    f.write(template)
    f.close()