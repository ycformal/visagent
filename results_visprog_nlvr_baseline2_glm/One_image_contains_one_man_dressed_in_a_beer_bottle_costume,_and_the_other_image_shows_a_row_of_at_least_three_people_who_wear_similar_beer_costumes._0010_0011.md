Question: One image contains one man dressed in a beer bottle costume, and the other image shows a row of at least three people who wear similar beer costumes.

Reference Answer: False

Left image URL: https://i.pinimg.com/originals/a5/52/61/a55261d54277e2d01f30c6a04343f280.jpg

Right image URL: https://i.pinimg.com/originals/4d/71/c5/4d71c53311621455136c26302a9fbc95.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image contains one man dressed in a beer bottle costume, and the other image shows a row of at least three people who wear similar beer costumes.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image contains one man dressed in a beer bottle costume, and the other image shows a row of at least three people who wear similar beer costumes.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

