Question: There is a human within one of the images.

Reference Answer: True

Left image URL: https://heirloomkayak.files.wordpress.com/2012/03/maggie-photo-op-spring-2012-009.jpg

Right image URL: http://www.fyneboatkits.co.uk/photos/products/sassafras/three-seat-sassafras-canoe.jpg

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

