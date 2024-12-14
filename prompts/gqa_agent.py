import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import tiktoken
import os
import io, tokenize
import numpy as np
# from engine.step_interpreters import parse_step

encoding = tiktoken.get_encoding("cl100k_base")

import gensim.downloader as api

# Load pre-trained GloVe embeddings
print('loading glove...')
glove = api.load("glove-wiki-gigaword-50")  # 50-dimensional vectors
print('glove loaded')

def sentence_to_vector(sentence, embedding_model):
    words = sentence.lower().split()
    word_vectors = [embedding_model[word] for word in words if word in embedding_model]
    if word_vectors:
        return np.mean(word_vectors, axis=0)
    else:
        return np.zeros(embedding_model.vector_size)  # Handle unseen words

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

files=[str(i) for i in range(1, 20)]
file_question_dict = {}
for file in files:
    file_path = os.path.join('./dataset_distilled', file + '.txt')
    with open(file_path, 'r') as f:
        text = f.read()
    context = text.split('<End of Context>')[0] + '<End of Context>'
    question = text.split('Q=')[1].split('\n')[0]
    question = question.strip('"')
    file_question_dict[file] = question

system_cmd = """
External modules in Implement:
LOC(image=*, object=*) returns bounding boxes for the specified object in the given image. Each bounding box is of the format [x1, y1, x2, y2], which represents the left top and right bottom of the rectangle. Note x axis grows horizontally from left to right, y axis grows vertically from top to bottom. Unit: pixels.
CROP(image=*, box=*,index=*) returns the cropped image within the specified bounding box. Only figure out things not included in the caption. If the answer is clear, use RESULT to output the answer.
CROP_RIGHTOF(image=*, box=*,index=*) returns the cropped image to the right of the specified bounding box.
CROP_LEFTOF(image=*, box=*,index=*)
CROP_ABOVE(image=*, box=*,index=*)
CROP_BELOW(image=*, box=*,index=*)
VQA(image=*, question=*) queries the Visual Question Answering system with a question about the image. Note: Responses may be brief and not fully accurate. You can use it to query attributes of an object that are not mentioned in the caption.
RESULT(var=*) only used in the last step. Returns the final result of the program. ONLY USE IT WHEN THE ANSWER IS CLEAR.
RELATIVE_POS(object=*, reference=*) returns the relative position of the object with respect to the reference object.
MERGE(box=*) merges bounding boxes into a single bounding box.
CAP(image=*) returns the caption of the image.
RETRIEVE(caption=*,question=*) retrieves useful information from the caption to answer the question. Only figure out things not included in the result. If the answer is clear, use RESULT to output the answer.
"""

def create_prompt_stepname_selective_efficient(inputs):
    global files
    global file_question_dict
    global vectorizer
    template = []
    file_score_dict = {}
    question = '"'.join(inputs['input'].split('<End of Context>')[0].split('Q=\"')[1].split('"')[:-1])

    for file in files:
        question_emb = sentence_to_vector(question, glove)
        file_question_emb = sentence_to_vector(file_question_dict[file], glove)
        similarity = cosine_similarity([question_emb], [file_question_emb])
        file_score_dict[file] = similarity[0][0]

    # sort files by text length, ascending
    _files = sorted(files, key=lambda x: file_score_dict[x], reverse=True)

    for file in _files:
        data = ''
        file_path = os.path.join('./dataset_distilled', file + '.txt')
        with open(file_path, 'r') as f:
            text = f.read()

        if '<result>' not in inputs['input']:
            data = 'Input:\n' + text.split('<End of Context>')[0] + '<End of Context>\nProgram:\n'
            data += text.split('<End of Context>')[1].split('<result>')[0].strip()
            template.append(data)
        else:
            last_Implement_statement = inputs['input'].strip().split('<result>')[-2].strip().split('\n')[-1].strip()
            step_name = parse_step(last_Implement_statement)['step_name']
            output_var = parse_step(last_Implement_statement)['output_var']
            step_count = text.count('=' + step_name + '(')
            if step_count == 0:
                continue
            random_step = random.randint(0, step_count - 1)
            prior_stepname = '</result>'.join(('=' + step_name + '(').join(text.split('=' + step_name + '(')[:random_step + 1]).split('</result>')[:-1])
            if prior_stepname == '':
                prior_stepname = '</result>'.join(('=' + step_name + '(').join(text.split('=' + step_name + '(')[:random_step + 1]).strip().split('<End of Context>')[:-1])
            post_stepname = ('=' + step_name + '(').join(text.split('=' + step_name + '(')[random_step + 1:])
            post_stepname = post_stepname.split('</result>')[0] + '</result>' + post_stepname.split('</result>')[1].split('<result>')[0]
            post_stepname = post_stepname.replace('<End of Plan>', '').strip()

            # Replace contents in <result></result> with "omitted", except the last occurrence
            import re
            def replace_result_content(text):
                pattern = r'(<result>)(.*?)(</result>\nThought)'
                text = re.sub(pattern, r'\1\nomitted\n\3', text, flags=re.DOTALL)
                return text

#             prior_stepname = replace_result_content(prior_stepname)

            data = 'Input:\n' + prior_stepname + '</result>\n' + output_var + '=' + step_name + '(' + '\n'.join(post_stepname.split('\n')[:-1]) + '\nProgram:\n' + post_stepname.split('\n')[-1]
            template.append(data)

        simulated_template = system_cmd + '\n' + '\n'.join(template) + '\n' + "{input}\n".format(**inputs)
        tokens = encoding.encode(simulated_template)
        if len(tokens) > 4096 - 512:
            template = template[:-1]
            break

    template = '\n'.join(template) + '\n'
    return system_cmd + '\n' + template + "Input:\n{input}\nProgram:\n".format(**inputs)