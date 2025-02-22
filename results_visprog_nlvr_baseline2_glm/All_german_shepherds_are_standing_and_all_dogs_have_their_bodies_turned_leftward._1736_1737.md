Question: All german shepherds are standing and all dogs have their bodies turned leftward.

Reference Answer: False

Left image URL: https://t3.ftcdn.net/jpg/00/01/58/56/500_F_1585679_sTqrEk8rFGGnfgYZaTU0sYeWhZ5TTV.jpg

Right image URL: https://i.pinimg.com/236x/fa/99/1a/fa991ae00a9b2b1d1ce88e28af04d17c--belgian-malinois-puppies-malinois-dog.jpg

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

