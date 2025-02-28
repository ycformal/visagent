Question: There are crabs inside an enclosed cage.

Reference Answer: True

Left image URL: http://1.bp.blogspot.com/-UB-WqMGM-Vw/VC0Tx4P1YkI/AAAAAAAAeN8/tDMsomsQB-M/s1600/IMG_0323.jpg

Right image URL: http://ww4.hdnux.com/photos/10/61/10/2298391/7/1024x1024.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are crabs inside an enclosed cage.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are crabs inside an enclosed cage.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

