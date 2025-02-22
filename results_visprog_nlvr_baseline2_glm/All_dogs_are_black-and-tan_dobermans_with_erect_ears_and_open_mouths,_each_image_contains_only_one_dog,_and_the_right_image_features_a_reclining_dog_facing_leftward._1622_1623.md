Question: All dogs are black-and-tan dobermans with erect ears and open mouths, each image contains only one dog, and the right image features a reclining dog facing leftward.

Reference Answer: True

Left image URL: https://howtotrainthedog.com/wp-content/uploads/2016/05/Do-Dobermans-Shed.jpg

Right image URL: https://howtotrainthedog.com/wp-content/uploads/2016/06/doberman-siting-in-field.jpg

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

