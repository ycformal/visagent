# for each file in results, get the answer in Answer: {...}

import os
import json
import re

def get_answer(file):
    if not os.path.exists(os.path.join('results_visprog', file)):
        print('File not found in results_visprog:', file)
        return 0, 0
    correct_visagent = 0
    correct = 0
    with open(os.path.join('results_visprog', file), 'r') as f:
        content = f.read()
        answer_visagent = re.search(r'\nAnswer: (.+)', content)
        try:
            answer_visagent = answer_visagent.group(1)
        except:
            print('Answer_visagent not found in', file)
            return 0, 0
        answer_visagent = answer_visagent.replace('.', '')
        answer_visagent = answer_visagent.replace(',', '')
        answer_visagent = answer_visagent.replace('"', '')
        answer_visagent = ' '.join(answer_visagent.split() + [word + 's' for word in answer_visagent.split()])
        reference = re.search(r'Reference Answer: (.+)', content)
        reference = reference.group(1)
        # print('Answer:', answer)
        # print('Reference:', reference)
        # split reference by non-alphanumeric characters
        reference = re.sub(r'\W+', ' ', reference)
        reference = ' '.join(reference.split() + [word + 's' for word in reference.split()])
        if len(set(answer_visagent.lower().split()).intersection(reference.lower().split())) > 0:
            # print('Correct')
            correct_visagent = 1
        else:
            # print('Incorrect')
            correct_visagent = 0
    with open(os.path.join('results', file), 'r') as f:
        content = f.read()
        answer = re.search(r'\nAnswer: (.+)', content)
        answer = answer.group(1)
        answer = answer.replace('.', '')
        answer = answer.replace(',', '')
        answer = answer.replace('"', '')
        answer = ' '.join(answer.split() + [word + 's' for word in answer.split()])
        reference = re.search(r'Reference Answer: (.+)', content)
        reference = reference.group(1)
        # print('Answer:', answer)
        # print('Reference:', reference)
        # split reference by non-alphanumeric characters
        reference = re.sub(r'\W+', ' ', reference)
        reference = ' '.join(reference.split() + [word + 's' for word in reference.split()])
        if len(set(answer.lower().split()).intersection(reference.lower().split())) > 0:
            # print('Correct')
            correct = 1
        else:
            # print('Incorrect')
            correct = 0
    if correct_visagent==1 and correct==0:
        print('Answer:', answer)
        print('Reference:', reference)
        print('Answer_visagent:', answer_visagent)
        print('\n')
    return correct_visagent, correct

def main():
    results_visagent = os.listdir('results_visagent')
    results = os.listdir('results')
    correct_visagent = 0
    total_visagent = 0
    correct = 0
    total = 0
    for result in results:
        correctness_visagent, correctness = get_answer(result)
        correct += correctness
        total += 1
        correct_visagent += correctness_visagent
        total_visagent += 1
        
    print('Correct: %d/%d' % (correct, total))
    print('Accuracy:', correct / total)
    print('Correct_visagent: %d/%d' % (correct_visagent, total_visagent))
    print('Accuracy_visagent:', correct_visagent / total_visagent)

if __name__ == '__main__':
    main()