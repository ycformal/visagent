Question: Each image includes three zebras posed in a row with their bodies parallel to one another.

Reference Answer: False

Left image URL: https://nrhatch.files.wordpress.com/2013/01/zebras.jpg

Right image URL: http://2.bp.blogspot.com/-3KKSX08PFDs/TgWziD6W_QI/AAAAAAAAAuA/dlx3BljYM_E/s400/6.jpg

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

