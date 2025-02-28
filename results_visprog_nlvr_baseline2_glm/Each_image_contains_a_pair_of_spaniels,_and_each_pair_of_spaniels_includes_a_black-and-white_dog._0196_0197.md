Question: Each image contains a pair of spaniels, and each pair of spaniels includes a black-and-white dog.

Reference Answer: True

Left image URL: https://www.kimballstock.com/pix/PUP/10/PUP-10-JE0033-01P.JPG

Right image URL: http://www.kimballstock.com/pix/PUP/10/PUP-10-JE0036-01P.JPG

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains a pair of spaniels, and each pair of spaniels includes a black-and-white dog.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains a pair of spaniels, and each pair of spaniels includes a black-and-white dog.' true or false?')=<b><span style='color: green;'>same</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>same</span></b></div><hr>

Answer: same

