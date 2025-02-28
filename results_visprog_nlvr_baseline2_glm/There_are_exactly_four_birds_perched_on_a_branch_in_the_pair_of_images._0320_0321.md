Question: There are exactly four birds perched on a branch in the pair of images.

Reference Answer: False

Left image URL: https://margaretlynettesharp.files.wordpress.com/2015/01/2013_1212imagefacebook0215.jpg

Right image URL: https://rowenasierant.files.wordpress.com/2015/09/rainbow-lorikeets-433436_1280.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are exactly four birds perched on a branch in the pair of images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are exactly four birds perched on a branch in the pair of images.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

