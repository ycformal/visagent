Question: All of the pelicans are on shore and none of them are extending their wings.

Reference Answer: True

Left image URL: https://c1.staticflickr.com/1/47/134969228_d52634c3fc_b.jpg

Right image URL: https://i.ytimg.com/vi/QNNl_uWmQXE/hqdefault.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'All of the pelicans are on shore and none of them are extending their wings.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All of the pelicans are on shore and none of them are extending their wings.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

