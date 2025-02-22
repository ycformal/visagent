# for each file in results, get the answer in Answer: {...}

import os
import json
import re
import shutil

data_NLVR2 = []
with open('./NLVR2/full/test1_filtered.json', 'r') as f:
  for line in f:
    data_NLVR2.append(json.loads(line))

def get_answer(file, method1, method2):
    if not os.path.exists(os.path.join(f'results_{method1}', file)):
        print(f'File not found in results_{method1}:', file)
        return 0, 0
    correct_1 = 0
    correct_2 = 0
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
        answer_1 = answer_1.replace('.', '')
        answer_1 = answer_1.replace(',', '')
        answer_1 = answer_1.replace('"', '')
        answer_1 = answer_1.replace('yes', 'true')
        answer_1 = answer_1.replace('no', 'false')
        answer_1 = answer_1.replace('Yes', 'true')
        answer_1 = answer_1.replace('No', 'false')
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
    with open(os.path.join(f'results_{method2}', file), 'r') as f:
        content = f.read()
        answer_2 = re.search(r'\nAnswer: (.+)', content)
        answer_2 = answer_2.group(1)
        answer_2 = answer_2.replace('.', '')
        answer_2 = answer_2.replace(',', '')
        answer_2 = answer_2.replace('"', '')
        answer_2 = answer_2.replace('yes', 'true')
        answer_2 = answer_2.replace('no', 'false')
        answer_2 = answer_2.replace('Yes', 'true')
        answer_2 = answer_2.replace('No', 'false')
        answer_2 = ' '.join(answer_2.split() + [word + 's' for word in answer_2.split()])
        reference = re.search(r'Reference Answer: (.+)', content)
        reference = reference.group(1)
        # split reference by non-alphanumeric characters
        reference = re.sub(r'\W+', ' ', reference)
        reference = ' '.join(reference.split() + [word + 's' for word in reference.split()])
        if len(set(answer_2.lower().split()).intersection(reference.lower().split())) > 0:
            correct_2 = 1
        else:
            correct_2 = 0
    if correct_1 == 1 and correct_2 == 0:
        print(f'{method1} correct, {method2} incorrect. Question: {question}')
    elif correct_1 == 0 and correct_2 == 1:
        print(f'{method1} incorrect, {method2} correct. Question: {question}')
    # os.makedirs(f'collection_both_false/{type}', exist_ok=True)
    # os.makedirs(f'collection_only_{method1}_true/{type}', exist_ok=True)
    # os.makedirs(f'collection_only_{method2}_true/{type}', exist_ok=True)
    # if correct_1==1 and correct_2==0:
    #     shutil.copyfile(os.path.join(f'results_{method1}', file), os.path.join(f'collection_only_{method1}_true/{type}', method1 + '_' + file))
    #     shutil.copyfile(os.path.join(f'results_{method2}', file), os.path.join(f'collection_only_{method1}_true/{type}', method2 + '_' + file))
    # elif correct_1==0 and correct_2==1:
    #     shutil.copyfile(os.path.join(f'results_{method1}', file), os.path.join(f'collection_only_{method2}_true/{type}', method1 + '_' + file))
    #     shutil.copyfile(os.path.join(f'results_{method2}', file), os.path.join(f'collection_only_{method2}_true/{type}', method2 + '_' + file))
    # elif correct_1==0 and correct_2==0:
    #     shutil.copyfile(os.path.join(f'results_{method1}', file), os.path.join(f'collection_both_false/{type}', method1 + '_' + file))
    #     shutil.copyfile(os.path.join(f'results_{method2}', file), os.path.join(f'collection_both_false/{type}', method2 + '_' + file))
    return correct_1, correct_2

def main():
    method1 = 'visprog_nlvr_baseline2_mistral'
    method2 = 'visprog_nlvr_mistral'
    results_1 = os.listdir(f'results_{method1}')
    results_2 = os.listdir(f'results_{method2}')
    correct_1 = 0
    total_1 = 0
    correct_2 = 0
    total_2 = 0
    for result in results_1:
        correctness_1, correctness_2 = get_answer(result, method1, method2)
        correct_1 += correctness_1
        total_1 += 1
        correct_2 += correctness_2
        total_2 += 1
        
    print(f'Correct_{method1}: {correct_1}/{total_1}')
    print(f'Accuracy_{method1}: {correct_1/total_1}')
    print(f'Correct_{method2}: {correct_2}/{total_2}')
    print(f'Accuracy_{method2}: {correct_2/total_2}')

if __name__ == '__main__':
    main()