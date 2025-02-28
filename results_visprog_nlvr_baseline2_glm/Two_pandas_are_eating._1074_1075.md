Question: Two pandas are eating.

Reference Answer: True

Left image URL: http://d2ouvy59p0dg6k.cloudfront.net/img/web_31203_359616.jpg

Right image URL: http://www.slate.com/content/dam/slate/articles/life/explainer/2012/10/121015_EXP_Panda.jpg.CROP.rectangle3-large.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Two pandas are eating.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Two pandas are eating.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

