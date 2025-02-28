Question: At least one of the dogs has its mouth open.

Reference Answer: True

Left image URL: https://img00.deviantart.net/13b0/i/2011/316/7/0/setus_black_and_white_border_collie_by_mineralss-d4fxvsz.jpg

Right image URL: http://d121tcdkpp02p4.cloudfront.net/clim/45923/Lloyd-2.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'At least one of the dogs has its mouth open.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one of the dogs has its mouth open.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

