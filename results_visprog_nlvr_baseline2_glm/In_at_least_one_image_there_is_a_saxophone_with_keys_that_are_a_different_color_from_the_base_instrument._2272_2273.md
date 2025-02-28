Question: In at least one image there is a saxophone with keys that are a different color from the base instrument.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/c1/ef/fc/c1effc6cdfb40ddfd77a854bc220d8fc--selmer-saxophone-saxophones.jpg

Right image URL: https://i.pinimg.com/736x/ce/84/1b/ce841ba66a4fc7fc7715f12127b0193b--saxophones.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image there is a saxophone with keys that are a different color from the base instrument.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image there is a saxophone with keys that are a different color from the base instrument.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

