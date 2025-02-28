Question: Three wine bottles with gold foil tops are stacked on a red mat.

Reference Answer: True

Left image URL: https://ae01.alicdn.com/kf/HTB1wLcTQXXXXXajXVXXq6xXFXXXE/Bottle-And-Can-Easy-Stacker-20-Pack-Stack-Water-Bottles-And-Food-Cans-Fit-More-On.jpg_120x120.jpg

Right image URL: http://img.auctiva.com/imgdata/1/9/0/7/5/2/4/webimg/843289090_tp.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Three wine bottles with gold foil tops are stacked on a red mat.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Three wine bottles with gold foil tops are stacked on a red mat.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

