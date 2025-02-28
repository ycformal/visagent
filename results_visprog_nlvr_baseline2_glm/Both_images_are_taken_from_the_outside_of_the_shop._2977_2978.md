Question: Both images are taken from the outside of the shop.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/ae/7d/9d/ae7d9dd6a9eff585a386228160d1e267.jpg

Right image URL: https://static1.squarespace.com/static/5320f028e4b0eaac35a6fa4f/54e2a11be4b02c194ef56eac/54ea24b3e4b01dbc2512f41e/1424654308349/Flour+City+Bakery.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Both images are taken from the outside of the shop.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Both images are taken from the outside of the shop.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

