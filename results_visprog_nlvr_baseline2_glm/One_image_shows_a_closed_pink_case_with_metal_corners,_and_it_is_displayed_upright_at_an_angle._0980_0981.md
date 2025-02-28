Question: One image shows a closed pink case with metal corners, and it is displayed upright at an angle.

Reference Answer: False

Left image URL: https://officedepot.scene7.com/is/image/officedepot/671053_p_wipo?$OD%2DLarge$&wid=450&hei=450

Right image URL: https://ae01.alicdn.com/kf/HTB1EyccKVXXXXbCXXXXq6xXFXXXm/Multi-function-cartoon-ABS-plastic-pencil-case-cute-password-lock-pencil-box-bag-with-calculator-escolar.jpg

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

