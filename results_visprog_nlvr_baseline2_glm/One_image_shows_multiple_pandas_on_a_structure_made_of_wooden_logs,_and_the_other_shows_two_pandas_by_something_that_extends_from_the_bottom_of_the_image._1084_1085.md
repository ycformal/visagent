Question: One image shows multiple pandas on a structure made of wooden logs, and the other shows two pandas by something that extends from the bottom of the image.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/68/01/a2/6801a2d4aa86e3c242aeb319d0f3d9b4--josh-red-pandas.jpg

Right image URL: https://i.pinimg.com/236x/42/cb/1c/42cb1cf1bc2c77c64eaebcd11bbbe978--giant-pandas-china.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows multiple pandas on a structure made of wooden logs, and the other shows two pandas by something that extends from the bottom of the image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows multiple pandas on a structure made of wooden logs, and the other shows two pandas by something that extends from the bottom of the image.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

