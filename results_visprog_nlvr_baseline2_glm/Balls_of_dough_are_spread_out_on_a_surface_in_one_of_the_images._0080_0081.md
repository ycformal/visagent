Question: Balls of dough are spread out on a surface in one of the images.

Reference Answer: True

Left image URL: https://www.maangchi.com/wp-content/uploads/2016/12/balloon-bread-shaping.jpg

Right image URL: https://www.maangchi.com/wp-content/uploads/2016/12/balloon-bread-dough-divide.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Balls of dough are spread out on a surface in one of the images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Balls of dough are spread out on a surface in one of the images.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

