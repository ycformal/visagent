Question: Each image contains one dog, with the one on the left posed with front paws forward, and the dog on the right showing some teeth.

Reference Answer: False

Left image URL: http://img.izismile.com/img/img4/20111229/640/these_funny_animals_872_640_12.jpg

Right image URL: https://kristieleephotography.files.wordpress.com/2016/12/bor-188-group.jpg?w=2000

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains one dog, with the one on the left posed with front paws forward, and the dog on the right showing some teeth.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains one dog, with the one on the left posed with front paws forward, and the dog on the right showing some teeth.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

