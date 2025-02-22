Question: The left and right image contains a total of two canopies, one square and one circle.

Reference Answer: False

Left image URL: https://images-na.ssl-images-amazon.com/images/I/51YC8Ev-7NL._SL500_AC_SS350_.jpg

Right image URL: https://i.pinimg.com/originals/a2/08/31/a20831a8557cced95b1ae6dc3aaa00d9.jpg

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

