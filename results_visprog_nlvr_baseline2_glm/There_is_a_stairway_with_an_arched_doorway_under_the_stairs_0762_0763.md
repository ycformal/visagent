Question: There is a stairway with an arched doorway under the stairs

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/2a/3d/22/2a3d22272ba88ec521c6cd392cd5db06--wrought-iron-spindles-railings-iron-railings-outdoor.jpg

Right image URL: https://i.pinimg.com/736x/e8/3e/c6/e83ec6199268e2f86b360a98b8867319--staircase-design-stair-spindles.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There is a stairway with an arched doorway under the stairs' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a stairway with an arched doorway under the stairs' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

