Question: One image shows a bouquet with gathered green stems but no vase, and the other image features a bouquet in a clear vase so the stems show through it.

Reference Answer: True

Left image URL: http://fyf.tac-cdn.net/images/products/large/BF82-11K.jpg

Right image URL: https://images-na.ssl-images-amazon.com/images/I/91hRtNtBVuL._SY550_.jpg

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

