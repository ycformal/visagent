Question: One image contains one man dressed in a beer bottle costume, and the other image shows a row of at least three people who wear similar beer costumes.

Reference Answer: True

Left image URL: https://images-na.ssl-images-amazon.com/images/I/51O6aWw2wOL._SY450_.jpg

Right image URL: https://images.maskworld.com/is/image/maskworld/bigview/flasche-bier-kostuem--mw-134688-2.jpg

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

