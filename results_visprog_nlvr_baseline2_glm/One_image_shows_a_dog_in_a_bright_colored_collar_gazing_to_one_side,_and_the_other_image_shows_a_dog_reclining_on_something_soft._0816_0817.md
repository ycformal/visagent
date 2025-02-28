Question: One image shows a dog in a bright colored collar gazing to one side, and the other image shows a dog reclining on something soft.

Reference Answer: True

Left image URL: https://i.pinimg.com/originals/52/e4/8f/52e48f87ef62eef434f2381cfa58f9d2.jpg

Right image URL: http://dogbreedstandards.com/wp-content/uploads/2012/01/Welsh-Terrier.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a dog in a bright colored collar gazing to one side, and the other image shows a dog reclining on something soft.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a dog in a bright colored collar gazing to one side, and the other image shows a dog reclining on something soft.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

