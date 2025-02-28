Question: There are three cell phones in total.

Reference Answer: True

Left image URL: https://www.phonedog.com/sites/phonedog.com/files/phone/large/samsung-sgh-t219-chocolate-2.jpg

Right image URL: https://images-na.ssl-images-amazon.com/images/I/715aZcsTN1L._SY679_.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are three cell phones in total.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are three cell phones in total.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

