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
    correct_1 = 0
    correct_2 = 0
    type = ''
    imageId = file.split('_')[-1].split('.')[0]
    with open(os.path.join(f'results_{method1}', file), 'r') as f:
        content = f.read()
        answer_1 = re.search(r'\nAnswer: (.+)', content)
        try:
            answer_1 = answer_1.group(1)
        except:
            print('answer_1 not found in', file)
            return 0, 0
        question = re.search(r'Question: (.+)', content)
        question = question.group(1).strip()
        type = data_dict[imageId][question]
        answer_1 = answer_1.replace('.', '')
        answer_1 = answer_1.replace(',', '')
        answer_1 = answer_1.replace('"', '')
        answer_1 = ' '.join(answer_1.split() + [word + 's' for word in answer_1.split()])
        reference = re.search(r'Reference Answer: (.+)', content)
        reference = reference.group(1)
        # split reference by non-alphanumeric characters
        reference = re.sub(r'\W+', ' ', reference)
        reference = ' '.join(reference.split() + [word + 's' for word in reference.split()])
        if len(set(answer_1.lower().split()).intersection(reference.lower().split())) > 0 and 'runtime error' not in answer_1.lower():
            correct_1 = 1
        else:
            correct_1 = 0
    return correct_1

def main():
    method1 = 'visprog'
    results_1 = os.listdir(f'results_{method1}')
    correct_1 = 0
    total_1 = 0
    for result in results_1:
        correctness_1 = get_answer(result, method1)
        correct_1 += correctness_1
        total_1 += 1
        
    print(f'Correct_{method1}: {correct_1}/{total_1}')
    print(f'Accuracy_{method1}: {correct_1/total_1}')

if __name__ == '__main__':
    main()