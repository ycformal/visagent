Question: One image shows a gauzy white canopy that drapes the front half of a bed from a cone shape suspended from the ceiling.

Reference Answer: True

Left image URL: https://vandytang.files.wordpress.com/2016/03/img_9082.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/25/79/b6/2579b6ef1491684ec2ac26a5773d3ba9.jpg

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

