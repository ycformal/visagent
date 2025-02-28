Question: One of the crabs is resting on sand.

Reference Answer: False

Left image URL: http://kenjonesfishing.com/wp-content/uploads/2012/01/cancer-antenarrius_ID_ODFW.jpg

Right image URL: http://kenjonesfishing.com/wp-content/uploads/2012/01/cancer_productus_ID_ODFW.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One of the crabs is resting on sand.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One of the crabs is resting on sand.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

