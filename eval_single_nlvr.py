# for each file in results, get the answer in Answer: {...}

import os
import json
import re
import shutil

data_NLVR2 = []
with open('./NLVR2/full/test1_filtered.json', 'r') as f:
  for line in f:
    data_NLVR2.append(json.loads(line))

def get_answer(file, method1):
    if not os.path.exists(os.path.join(f'results_{method1}', file)):
        print(f'File not found in results_{method1}:', file)
        return 0
    correct = 0
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
        answer = answer.replace('.', '')
        answer = answer.replace(',', '')
        answer = answer.replace('"', '')
        answer = answer.replace('yes', 'true')
        answer = answer.replace('no', 'false')
        answer = answer.replace('Yes', 'true')
        answer = answer.replace('No', 'false')
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
    method = 'visprog_nlvr_baseline2_gpt'
    results = os.listdir(f'results_{method}')
    correct = 0
    total = 0
    for result in results:
        correctness = get_answer(result, method)
        correct += correctness
        total += 1
        
    print(f'Correct_{method}: {correct}/{total}')
    print(f'Accuracy_{method}: {correct/total}')

    method = 'visprog_nlvr_baseline2_mistral'
    results = os.listdir(f'results_{method}')
    correct = 0
    total = 0
    for result in results:
        correctness = get_answer(result, method)
        correct += correctness
        total += 1
        
    print(f'Correct_{method}: {correct}/{total}')
    print(f'Accuracy_{method}: {correct/total}')

    method = 'visprog_nlvr_baseline2_glm'
    results = os.listdir(f'results_{method}')
    correct = 0
    total = 0
    for result in results:
        correctness = get_answer(result, method)
        correct += correctness
        total += 1
        
    print(f'Correct_{method}: {correct}/{total}')
    print(f'Accuracy_{method}: {correct/total}')

    method = 'visprog_nlvr_baseline2_llama'
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