Question: One image shows three side-by-side gray-and-white husky puppies in upright sitting poses, and all dogs in both images are puppies.

Reference Answer: True

Left image URL: http://st2.depositphotos.com/1283307/11423/v/450/depositphotos_114230118-stock-video-close-up-three-calm-fluffy.jpg

Right image URL: https://www.kimballstock.com/pix/PUP/02/PUP-02-CB0001-01P.JPG

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

