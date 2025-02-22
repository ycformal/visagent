Question: One image shows a bouquet with gathered green stems but no vase, and the other image features a bouquet in a clear vase so the stems show through it.

Reference Answer: False

Left image URL: https://images-na.ssl-images-amazon.com/images/I/51CgQ4mgg3L.jpg

Right image URL: http://www.brantflorist.com/images/Products/BF2455_t.jpg

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

