Question: One image shows a closed pink case with metal corners, and it is displayed upright at an angle.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/33/64/89/33648965a621ec34d90ad733b00f61e3.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1TRl5PXXXXXaaXFXXq6xXFXXXZ/Multi-function-cartoon-ABS-plastic-font-b-pencil-b-font-case-cute-password-font-b-lock.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a closed pink case with metal corners, and it is displayed upright at an angle.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a closed pink case with metal corners, and it is displayed upright at an angle.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

