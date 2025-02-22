Question: One image shows a neat row of three guinea pigs, all with different coloring.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/97/50/bf/9750bf76fedfc893fca53fe0cbad9245--smiling-animals-baby-animals.jpg

Right image URL: https://i.pinimg.com/736x/ba/02/95/ba029580fd064f409d9fffab50a185cb--three-little-pigs-cavi.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

