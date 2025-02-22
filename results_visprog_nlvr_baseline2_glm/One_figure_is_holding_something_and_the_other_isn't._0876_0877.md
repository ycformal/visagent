Question: One figure is holding something and the other isn't.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/1d/25/b8/1d25b8daeb265e0dd8d36f00324b41c9.jpg

Right image URL: http://facultycapsandgowns.com/images/PhD_gown_goldpiping.jpg

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

