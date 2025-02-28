Question: In one image, the dessert is near a red and white cloth.

Reference Answer: True

Left image URL: https://i2.wp.com/www.livewellbakeoften.com/wp-content/uploads/2016/06/No-Bake-Strawberry-and-Blueberry-Cheesecake-Trifle-10.jpg?resize=680%2C1020&ssl=1

Right image URL: https://lh3.googleusercontent.com/sGl9Vv-xax3Bz6GXj_NLvMmDI5xIsfzJ4MfLEYbnNbH6Rn_IdxAyoxHrd5wAgzsZkknUXt2uG8Q2w6pasp95bdiZIczjt44DFQIwiqhB=w600-l68

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
ANSWER0=VQA(image=IMAGE,question="Is 'In one image, the dessert is near a red and white cloth.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In one image, the dessert is near a red and white cloth.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

