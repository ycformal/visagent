Question: An image includes mostly forward-facing graduates wearing pale blue sashes across their bodies.

Reference Answer: False

Left image URL: https://www.odt.co.nz/sites/default/files/story/2016/04/grad_2_101214_jpg_5488146eb4.JPG

Right image URL: https://www.odt.co.nz/sites/default/files/story/2016/04/waving_to_friends_as_they_take_part_in_the_univers_5007880614.JPG

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
ANSWER0=VQA(image=IMAGE,question="Is 'An image includes mostly forward-facing graduates wearing pale blue sashes across their bodies.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image includes mostly forward-facing graduates wearing pale blue sashes across their bodies.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

