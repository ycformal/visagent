Question: Each image contains at least one inflated balloon, but the lefthand image contains a greater number of inflated balloons.

Reference Answer: True

Left image URL: https://fthmb.tqn.com/SnVnByodsUwGjvHOVOJvM68lZpQ=/768x0/filters:no_upscale():max_bytes(150000):strip_icc()/birthday-balloons-58bacea53df78c353c45b186.jpg

Right image URL: https://cdn.asme.org/getmedia/0f24a9ca-2671-43f3-8874-7e0ba028b151/air_pressure_baloons.jpg.aspx

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains at least one inflated balloon, but the lefthand image contains a greater number of inflated balloons.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains at least one inflated balloon, but the lefthand image contains a greater number of inflated balloons.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

