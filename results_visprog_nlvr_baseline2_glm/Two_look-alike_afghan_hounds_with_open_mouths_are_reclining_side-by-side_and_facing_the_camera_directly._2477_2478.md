Question: Two look-alike afghan hounds with open mouths are reclining side-by-side and facing the camera directly.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/84/fa/42/84fa428be7281a6b96e6da01d08984fb--the-very-the-ojays.jpg

Right image URL: https://images.puppyfinder.com/Breed/2/6/7/267b3f72e54ca08d_AfghanHound2_medium.jpg

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

