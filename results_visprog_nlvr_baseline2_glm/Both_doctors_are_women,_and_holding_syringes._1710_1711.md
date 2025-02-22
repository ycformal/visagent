Question: Both doctors are women, and holding syringes.

Reference Answer: False

Left image URL: https://static6.depositphotos.com/1085342/582/i/950/depositphotos_5821536-stock-photo-crazy-doctor-nerd.jpg

Right image URL: http://watermarked.cutcaster.com/cutcaster-photo-100136780-Scary-doctor.jpg

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

