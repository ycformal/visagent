Question: One image shows a canopy suspended from the ceiling that drapes the headboard end of the bed from a cone shape.

Reference Answer: True

Left image URL: https://i.pinimg.com/originals/8b/17/66/8b17667d5941baae0fc1b67af55d20e6.jpg

Right image URL: https://i.pinimg.com/originals/23/05/4e/23054e3c331003c77b5d2c3d5dc555f1.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a canopy suspended from the ceiling that drapes the headboard end of the bed from a cone shape.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a canopy suspended from the ceiling that drapes the headboard end of the bed from a cone shape.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

