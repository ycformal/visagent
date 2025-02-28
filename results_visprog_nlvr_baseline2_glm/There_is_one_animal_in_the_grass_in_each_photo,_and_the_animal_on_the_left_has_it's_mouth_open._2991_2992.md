Question: There is one animal in the grass in each photo, and the animal on the left has it's mouth open.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/50/37/91/503791fcae9c36c78d77ca37da97db91.jpg

Right image URL: http://1.bp.blogspot.com/_f98opUNuVXc/TEc9uhL57UI/AAAAAAAARA0/duJnaIkIq-Q/s400/Baby+skunk.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There is one animal in the grass in each photo, and the animal on the left has it's mouth open.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is one animal in the grass in each photo, and the animal on the left has it's mouth open.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

