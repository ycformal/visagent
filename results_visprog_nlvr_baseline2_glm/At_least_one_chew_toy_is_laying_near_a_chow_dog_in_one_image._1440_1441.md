Question: At least one chew toy is laying near a chow dog in one image.

Reference Answer: True

Left image URL: http://www.chow-dalen.ru/dogs/arven/arven5.jpg

Right image URL: https://i.ytimg.com/vi/B1Q1x-1V81k/maxresdefault.jpg

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

