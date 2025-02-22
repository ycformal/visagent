Question: One image shows one plastic-wrapped rectangle containing at least 50 paper rolls, with packs containing less than 20 total rolls stacked on top.

Reference Answer: True

Left image URL: https://sc01.alicdn.com/kf/HTB1utE1FFXXXXcBaFXXq6xXFXXXx/200339910/HTB1utE1FFXXXXcBaFXXq6xXFXXXx.jpg

Right image URL: https://sc01.alicdn.com/kf/HTB1JkN_LVXXXXclXFXX760XFXXXb/wholesale-bulk-toilet-tissue-soft-paper-with.png

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

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

