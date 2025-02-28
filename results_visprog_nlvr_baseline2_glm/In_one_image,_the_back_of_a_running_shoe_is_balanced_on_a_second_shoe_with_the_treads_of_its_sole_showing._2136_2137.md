Question: In one image, the back of a running shoe is balanced on a second shoe with the treads of its sole showing.

Reference Answer: False

Left image URL: https://ae01.alicdn.com/kf/HTB1XBf.LpXXXXadXpXXq6xXFXXXz/Q7-marca-v-lei-basquete-esportes-el-stico-de-borracha-anti-colis-o-joelho-cinza-claro.jpg_640x640.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1wnZRaBUSMeJjSszbq6zerFXa6/3D-Tkania-Silikonowe-Ochraniacze-Sportowe-Siatk-wka-Nakolanniki-Obs-uguje-Brace-Rzepki-Koszyk-wki-kotki-Kneepads.jpg_640x640.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In one image, the back of a running shoe is balanced on a second shoe with the treads of its sole showing.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In one image, the back of a running shoe is balanced on a second shoe with the treads of its sole showing.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

