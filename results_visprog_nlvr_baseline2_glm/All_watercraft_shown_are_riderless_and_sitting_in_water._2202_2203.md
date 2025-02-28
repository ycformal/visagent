Question: All watercraft shown are riderless and sitting in water.

Reference Answer: False

Left image URL: https://i.pinimg.com/originals/c5/ee/ea/c5eeea9c0d0676cbc045d0deab9b3d03.jpg

Right image URL: https://i.pinimg.com/originals/26/7d/4a/267d4a3c2a4b22c57ceb8a7b79e9c534.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'All watercraft shown are riderless and sitting in water.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All watercraft shown are riderless and sitting in water.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

