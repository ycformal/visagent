import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import tiktoken
import os
from engine.step_interpreters import parse_step

nltk.download('punkt')
nltk.download('stopwords')
vectorizer = TfidfVectorizer()
encoding = tiktoken.get_encoding("cl100k_base")

# Function to preprocess text
def preprocess(text):
    # Tokenize text
    tokens = word_tokenize(text.lower())  # Convert to lower case and tokenize
    # Remove stopwords
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return " ".join(tokens)

def longest_common_prefix(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]

files=[str(i) for i in range(1, 60)]
file_question_dict = {}
for file in files:
    file_path = os.path.join('./dataset_revised', file + '.txt')
    with open(file_path, 'r') as f:
        text = f.read()
    context = text.split('<End of Context>')[0] + '<End of Context>'
    question = text.split('Q=')[1].split('\n')[0]
    question = question.strip('"')
    file_question_dict[file] = question

system_cmd = """
External modules in Implement:
LOC(image=*, object=*) returns bounding boxes for the specified object in the given image. Each bounding box is of the format [x1, y1, x2, y2], which represents the left top and right bottom of the rectangle. Note x axis grows horizontally from left to right, y axis grows vertically from top to bottom. Unit: pixels.
COUNT(box=*) returns the total number of specified bounding boxes.
CROP(image=*, box=*,index=*) returns the cropped image within the specified bounding box.
CROP_RIGHTOF(image=*, box=*,index=*) returns the cropped image to the right of the specified bounding box.
CROP_LEFTOF(image=*, box=*,index=*)
CROP_ABOVE(image=*, box=*,index=*)
CROP_BELOW(image=*, box=*,index=*)
VQA(image=*, question=*) queries the Visual Question Answering system with a question about the image. Note: Responses may be brief and not fully accurate.
RESULT(var=*) only used in the last step. Returns the final result of the program.
"""

def create_prompt_full(inputs, print_template=False):
    global files
    global file_question_dict
    global vectorizer
    num_examples = 12
    mode = 'beginning'
    if 'End of Plan' in inputs['input']:
        mode = 'middle'
    if mode != 'beginning':
        num_examples = 5
    template = ''
    file_score_dict = {}
    for file in files:
        tfidf_matrix = vectorizer.fit_transform([inputs['input'], file_question_dict[file]])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        file_score_dict[file] = similarity[0][0]
    files = sorted(files, key=lambda x: file_score_dict[x], reverse=True)
    for file in files[1:num_examples]:
        file_path = os.path.join('./dataset_revised', file + '.txt')
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
            assert '=' in statement and '(' in statement.split('=')[1] and ')' == statement[-1]
            template += 'Input:\n' + current_context + '\nOutput:\n' + response + '\n'
            while next_line < len(steps) and '</result>' not in steps[next_line]:
                if 'Thought(' in steps[next_line]:
                    raise Exception(f'{file}.txt: <result> is not closed')
                next_line += 1
            next_line += 1
            if mode == 'beginning':
                break
    if print_template:
        print(template)
    return template + "Input: {input}\nOutput:\n".format(**inputs)

def create_prompt_simple(inputs, print_template=False):
    global files
    global file_question_dict
    global vectorizer
    num_examples = 3
    mode = 'beginning'
    if 'End of Plan' in inputs['input']:
        mode = 'middle'
    if mode != 'beginning':
        num_examples = 3
    template = ''
    file_score_dict = {}
    for file in files:
        tfidf_matrix = vectorizer.fit_transform([inputs['input'], file_question_dict[file]])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        file_score_dict[file] = similarity[0][0]
    files = sorted(files, key=lambda x: file_score_dict[x], reverse=True)
    for file in files[:num_examples]:
        file_path = os.path.join('./dataset_revised', file + '.txt')
        with open(file_path, 'r') as f:
            text = f.read()
        template += text + '\n'
    if print_template:
        print(template)
    return template + "Input: {input}\nOutput:\n".format(**inputs)

def create_prompt_layered(inputs, print_template=False):
    global files
    global file_question_dict
    global vectorizer
    template = []
    file_score_dict = {}
    for file in files:
        tfidf_matrix = vectorizer.fit_transform([inputs['input'], file_question_dict[file]])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        file_score_dict[file] = similarity[0][0]
    files = sorted(files, key=lambda x: file_score_dict[x], reverse=True)
    for file in files:
        data = ''
        file_path = os.path.join('./dataset_revised', file + '.txt')
        with open(file_path, 'r') as f:
            text = f.read()
        if 'Implement' not in inputs['input']:
            data = text.split('<End of Context>')[0] + '<End of Context>'
            data += text.split('<End of Context>')[1].split('Implement(')[0]+ 'Implement(' + text.split('Implement(')[1].split('))\n')[0] + '))\n\n<End of Plan>'
            template.append(data)
        else:
            n_Implement = inputs['input'].count('Implement(')
            if text.count('Implement(') < n_Implement + 1:
                data = text
                template.append(data)
            else:
                data = 'Implement('.join(text.split('Implement(')[:n_Implement + 1]) + text.split('Implement(')[n_Implement + 1].split('))\n')[0] + '))\n\n<End of Plan>'
                template.append(data)
        simulated_template = system_cmd + '\n' + '\n'.join(template) + '\n' + "{input}\n".format(**inputs)
        tokens = encoding.encode(simulated_template)
        if len(tokens) > 4096 - 512:
            template = template[:-1]
            break
    template = '\n'.join(template) + '\n'
    if print_template:
        print(template)
    return system_cmd + '\n' + template + "{input}\n".format(**inputs)

def create_prompt_stepname(inputs,  print_template=False):
    global files
    global file_question_dict
    global vectorizer
    template = []
    file_score_dict = {}
    for file in files:
        tfidf_matrix = vectorizer.fit_transform([inputs['input'], file_question_dict[file]])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        file_score_dict[file] = similarity[0][0]
    files = sorted(files, key=lambda x: len(open(f'./dataset_revised/{x}.txt').read()))[10:30]
    files = sorted(files, key=lambda x: file_score_dict[x], reverse=True)
    for file in files:
        data = ''
        file_path = os.path.join('./dataset_revised', file + '.txt')
        with open(file_path, 'r') as f:
            text = f.read()
        if 'Implement' not in inputs['input']:
            data = text.split('<End of Context>')[0] + '<End of Context>'
            data += text.split('<End of Context>')[1].split('Implement(')[0]+ 'Implement(' + text.split('Implement(')[1].split('))\n')[0] + '))\n\n<End of Plan>'
            template.append(data)
        else:
            n_Implement = inputs['input'].count('Implement(')
            last_Implement_statement = inputs['input'].split('Implement(')[n_Implement].split('))\n')[0] + ')'
            step_name = parse_step(last_Implement_statement)['step_name']
            step_count = text.count('=' + step_name + '(')
            if step_count == 0:
                continue
            random_step = random.randint(0, step_count - 1)
            prior_stepname = 'Implement('.join(('=' + step_name + '(').join(text.split('=' + step_name + '(')[:random_step + 1]).split('Implement(')[:-1])
            post_stepname = ('=' + step_name + '(').join(text.split('=' + step_name + '(')[random_step + 1:])
            post_stepname = post_stepname.split('Implement(')[0] + 'Implement(' + post_stepname.split('Implement(')[1].split('))\n')[0] + '))\n\n<End of Plan>'
            data = prior_stepname + '=' + step_name + '(' + post_stepname
            template.append(data)
        simulated_template = system_cmd + '\n' + '\n'.join(template) + '\n' + "{input}\n".format(**inputs)
        tokens = encoding.encode(simulated_template)
        if len(tokens) > 4096 - 512:
            template = template[:-1]
            break
    template = '\n'.join(template) + '\n'
    if print_template:
        print(template)
    return system_cmd + '\n' + template + "{input}\n".format(**inputs)


def create_prompt_stepname_selective(inputs, print_template=False):
    global files
    global file_question_dict
    global vectorizer
    template = []
    file_score_dict = {}

    for file in files:
        tfidf_matrix = vectorizer.fit_transform([inputs['input'], file_question_dict[file]])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        file_score_dict[file] = similarity[0][0]

    files = sorted(files, key=lambda x: file_score_dict[x], reverse=True)

    for file in files:
        data = ''
        file_path = os.path.join('./dataset_revised', file + '.txt')
        with open(file_path, 'r') as f:
            text = f.read()

        if 'Implement' not in inputs['input']:
            data = text.split('<End of Context>')[0] + '<End of Context>'
            data += text.split('<End of Context>')[1].split('Implement(')[0]+ 'Implement(' + \
                    text.split('Implement(')[1].split('))\n')[0] + '))\n\n<End of Plan>'
            template.append(data)
        else:
            n_Implement = inputs['input'].count('Implement(')
            last_Implement_statement = inputs['input'].split('Implement(')[n_Implement].split('))\n')[0] + ')'
            step_name = parse_step(last_Implement_statement)['step_name']
            output_var = parse_step(last_Implement_statement)['output_var']
            step_count = text.count('=' + step_name + '(')
            if step_count == 0:
                continue
            random_step = random.randint(0, step_count - 1)
            prior_stepname = 'Implement('.join(('=' + step_name + '(').join(text.split('=' + step_name + '(')[:random_step + 1]).split('Implement(')[:-1])
            post_stepname = ('=' + step_name + '(').join(text.split('=' + step_name + '(')[random_step + 1:])
            post_stepname = post_stepname.split('Implement(')[0] + 'Implement(' + post_stepname.split('Implement(')[1].split('))\n')[0] + '))\n\n<End of Plan>'

            # Replace contents in <result></result> with "omitted", except the last occurrence
            import re
            def replace_result_content(text):
                pattern = r'(<result>)(.*?)(</result>\nThought)'
                text = re.sub(pattern, r'\1\nomitted\n\3', text, flags=re.DOTALL)
                return text

            prior_stepname = replace_result_content(prior_stepname)

            # Replace content in CAPTION_IMAGE=""
            def replace_caption_image_content(text):
                pattern = r'CAPTION_IMAGE="(.*?)"\n\nQ='
                match = re.search(pattern, text, re.DOTALL)
                if match:
                    start, end = match.span(1)
                    text = text[:start] + 'omitted' + text[end:]
                return text

            prior_stepname = replace_caption_image_content(prior_stepname)

            data = prior_stepname + 'Implement(' + output_var + '=' + step_name + '(' + post_stepname
            template.append(data)

        simulated_template = system_cmd + '\n' + '\n'.join(template) + '\n' + "{input}\n".format(**inputs)
        tokens = encoding.encode(simulated_template)
        if len(tokens) > 4096 - 512:
            template = template[:-1]
            break

    template = '\n'.join(template) + '\n'
    if print_template:
        print(template)
    return system_cmd + '\n' + template + "{input}\n".format(**inputs)

def create_prompt_stepname_selective_efficient(inputs):
    global files
    global file_question_dict
    global vectorizer
    template = []
    file_score_dict = {}

    for file in files:
        tfidf_matrix = vectorizer.fit_transform([inputs['input'], file_question_dict[file]])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        file_score_dict[file] = similarity[0][0]

    
    # sort files by text length, ascending
    indices = [0,1,2,10,11,12,13,20,21,22,23,25,25,26,27,28,29,30,40,50]
    files = sorted(files, key=lambda x: len(open(f'./dataset_revised/{x}.txt').read()))
    files = [files[i] for i in indices]
    files = sorted(files, key=lambda x: file_score_dict[x], reverse=True)

    for file in files:
        data = ''
        file_path = os.path.join('./dataset_revised', file + '.txt')
        with open(file_path, 'r') as f:
            text = f.read()

        if 'Implement' not in inputs['input']:
            data = text.split('<End of Context>')[0] + '<End of Context>'
            data += text.split('<End of Context>')[1].split('Implement(')[0]+ 'Implement(' + \
                    text.split('Implement(')[1].split('))\n')[0] + '))\n\n<End of Plan>'
            template.append(data)
        else:
            n_Implement = inputs['input'].count('Implement(')
            last_Implement_statement = inputs['input'].split('Implement(')[n_Implement].split('))\n')[0] + ')'
            step_name = parse_step(last_Implement_statement)['step_name']
            output_var = parse_step(last_Implement_statement)['output_var']
            step_count = text.count('=' + step_name + '(')
            if step_count == 0:
                continue
            random_step = random.randint(0, step_count - 1)
            prior_stepname = 'Implement('.join(('=' + step_name + '(').join(text.split('=' + step_name + '(')[:random_step + 1]).split('Implement(')[:-1])
            post_stepname = ('=' + step_name + '(').join(text.split('=' + step_name + '(')[random_step + 1:])
            post_stepname = post_stepname.split('Implement(')[0] + 'Implement(' + post_stepname.split('Implement(')[1].split('))\n')[0] + '))\n\n<End of Plan>'

            # Replace contents in <result></result> with "omitted", except the last occurrence
            import re
            def replace_result_content(text):
                pattern = r'(<result>)(.*?)(</result>\nThought)'
                text = re.sub(pattern, r'\1\nomitted\n\3', text, flags=re.DOTALL)
                return text

            prior_stepname = replace_result_content(prior_stepname)

            # Replace content in CAPTION_IMAGE=""
            def replace_caption_image_content(text):
                pattern = r'CAPTION_IMAGE="(.*?)"\n\nQ='
                match = re.search(pattern, text, re.DOTALL)
                if match:
                    start, end = match.span(1)
                    text = text[:start] + 'omitted' + text[end:]
                return text

            prior_stepname = replace_caption_image_content(prior_stepname)

            data = prior_stepname + 'Implement(' + output_var + '=' + step_name + '(' + post_stepname
            template.append(data)

        simulated_template = system_cmd + '\n' + '\n'.join(template) + '\n' + "{input}\n".format(**inputs)
        tokens = encoding.encode(simulated_template)
        if len(tokens) > 4096 - 512:
            template = template[:-1]
            break

    template = '\n'.join(template) + '\n'
    return system_cmd + '\n' + template + "{input}\n".format(**inputs)