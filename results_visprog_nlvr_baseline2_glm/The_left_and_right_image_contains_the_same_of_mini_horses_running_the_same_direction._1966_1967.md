Question: The left and right image contains the same of mini horses running the same direction.

Reference Answer: False

Left image URL: http://www.angelfire.com/pa5/hiddentimber/images/cart_in_use.jpg

Right image URL: https://i.pinimg.com/originals/20/bf/fd/20bffd9414c5abda96d38736f910a0ef.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains the same of mini horses running the same direction.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains the same of mini horses running the same direction.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

