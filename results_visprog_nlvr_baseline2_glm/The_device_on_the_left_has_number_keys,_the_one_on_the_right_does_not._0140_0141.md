Question: The device on the left has number keys, the one on the right does not.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/d4/fd/23/d4fd239ac635b3b667dab2d9094481f2--dual-sim-phone-cases.jpg

Right image URL: https://i.pinimg.com/736x/21/0c/66/210c66bdec1e5a8db90bd4ef98c593db---month-smartphone.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The device on the left has number keys, the one on the right does not.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The device on the left has number keys, the one on the right does not.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

