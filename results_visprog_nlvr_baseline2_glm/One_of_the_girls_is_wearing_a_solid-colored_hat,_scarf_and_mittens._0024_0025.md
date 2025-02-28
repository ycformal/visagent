Question: One of the girls is wearing a solid-colored hat, scarf and mittens.

Reference Answer: True

Left image URL: http://10.china-cart.com/10_accessories_scarves_hats_gloves_caps/1309948812/alb/1309948812_12242.jpg

Right image URL: http://10.china-cart.com/10_accessories_scarves_hats_gloves_caps/1332227065/alb/1332227065_2414.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One of the girls is wearing a solid-colored hat, scarf and mittens.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One of the girls is wearing a solid-colored hat, scarf and mittens.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

