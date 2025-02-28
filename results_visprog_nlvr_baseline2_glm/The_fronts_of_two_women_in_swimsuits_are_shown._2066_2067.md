Question: The fronts of two women in swimsuits are shown.

Reference Answer: True

Left image URL: https://i.pinimg.com/originals/f8/71/b9/f871b90cbac1952afc3683e54944cd35.jpg

Right image URL: https://i.pinimg.com/originals/ff/80/b7/ff80b7f94873994706661d996a3291ed.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The fronts of two women in swimsuits are shown.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The fronts of two women in swimsuits are shown.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

