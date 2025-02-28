Question: One of the images shows exactly two ferrets interacting with each other: one white/blond and one dark.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/wRCCZVhLZI8/maxresdefault.jpg

Right image URL: https://i.pinimg.com/736x/96/63/14/966314c738b9059cab74efc379d90bf7--ferrets-adorable-animals.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One of the images shows exactly two ferrets interacting with each other: one white/blond and one dark.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One of the images shows exactly two ferrets interacting with each other: one white/blond and one dark.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

