Question: One image shows a baboon holding a fruit to its mouth, and one image shows a baboon with a wide-open mouth baring fangs.

Reference Answer: True

Left image URL: http://4.bp.blogspot.com/-XiCNNSCZiyA/T06NMHHsV9I/AAAAAAAAADo/U4pFbWlU4Kk/s1600/Baboonteeth.jpg

Right image URL: http://static8.depositphotos.com/1418420/890/i/950/depositphotos_8902914-Baboon-eating-fruit.jpg

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

