Question: One image contains two stacks of towels, and all towels are different solid colors and shades of colors.

Reference Answer: False

Left image URL: https://ae01.alicdn.com/kf/HTB1FhbLQXXXXXc9aXXXq6xXFXXX3/3-unids-lote-Toallas-de-Cara-del-Algod-n-a-cuadros-grandes-de-rect-ngulo-hotel.jpg_640x640.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1KocrIpXXXXXCaXXXq6xXFXXXE/Japon-s-fresco-de-color-claro-de-algod-n-gruesas-toallas-grandes-toallas-de-ba-o.jpg_640x640.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>towel</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>towel</span></b></div><hr>

Answer: towel

