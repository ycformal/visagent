# for each file in results, get the answer in Answer: {...}

import os
import json
import re
import shutil

with open('sampled_GQA/sampled_data.json', 'r') as f:
    sampled_data = json.load(f)

data_dict = {}

for data in sampled_data:
    question = data['question']
    imageId = data['imageId']
    type = data['type']
    if imageId not in data_dict:
        data_dict[imageId] = {question: type}
    else:
        data_dict[imageId][question] = type

def get_answer(file, method1):
    if not os.path.exists(os.path.join(f'results_{method1}', file)):
        print(f'File not found in results_{method1}:', file)
        return 0
    correct = 0
    type = ''
    imageId = file.split('_')[-1].split('.')[0]
    with open(os.path.join(f'results_{method1}', file), 'r') as f:
        content = f.read()
        answer = re.search(r'\nAnswer: (.+)', content)
        try:
            answer = answer.group(1)
        except:
            print('answer not found in', file)
            return 0
        question = re.search(r'Question: (.+)', content)
        question = question.group(1).strip()
        type = data_dict[imageId][question]
        answer = answer.replace('.', '')
        answer = answer.replace(',', '')
        answer = answer.replace('"', '')
        answer = ' '.join(answer.split() + [word + 's' for word in answer.split()])
        reference = re.search(r'Reference Answer: (.+)', content)
        reference = reference.group(1)
        # split reference by non-alphanumeric characters
        reference = re.sub(r'\W+', ' ', reference)
        reference = ' '.join(reference.split() + [word + 's' for word in reference.split()])
        if len(set(answer.lower().split()).intersection(reference.lower().split())) > 0 and 'runtime error' not in answer.lower():
            correct = 1
        else:
            correct = 0
    return correct

def main():
    method = 'baseline2_v2_gpt'
    results = os.listdir(f'results_{method}')
    correct = 0
    total = 0
    for result in results:
        correctness = get_answer(result, method)
        correct += correctness
        total += 1
        
    print(f'Correct_{method}: {correct}/{total}')
    print(f'Accuracy_{method}: {correct/total}')

    method = 'baseline2_v2_mistral'
    results = os.listdir(f'results_{method}')
    correct = 0
    total = 0
    for result in results:
        correctness = get_answer(result, method)
        correct += correctness
        total += 1
        
    print(f'Correct_{method}: {correct}/{total}')
    print(f'Accuracy_{method}: {correct/total}')

    method = 'baseline2_v2_glm'
    results = os.listdir(f'results_{method}')
    correct = 0
    total = 0
    for result in results:
        correctness = get_answer(result, method)
        correct += correctness
        total += 1
        
    print(f'Correct_{method}: {correct}/{total}')
    print(f'Accuracy_{method}: {correct/total}')

    method = 'baseline2_v2_llama'
    results = os.listdir(f'results_{method}')
    correct = 0
    total = 0
    for result in results:
        correctness = get_answer(result, method)
        correct += correctness
        total += 1
        
    print(f'Correct_{method}: {correct}/{total}')
    print(f'Accuracy_{method}: {correct/total}')

if __name__ == '__main__':
    main()