Question: Each image contains a single dog, and the right image shows a basset hound facing forward with an open mouth showing its tongue.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/46/65/9a/46659adddc31fb25400ebf87a630dcd8--basset-hound-funny-hound-dog.jpg

Right image URL: https://i.pinimg.com/736x/c8/0d/ba/c80dbaf3078ecb4143113d0606369686--rogues-lemon.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains a single dog, and the right image shows a basset hound facing forward with an open mouth showing its tongue.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains a single dog, and the right image shows a basset hound facing forward with an open mouth showing its tongue.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

