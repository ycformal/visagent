Question: One image contains one man dressed in a beer bottle costume, and the other image shows a row of at least three people who wear similar beer costumes.

Reference Answer: True

Left image URL: https://i.pinimg.com/originals/fc/5c/f1/fc5cf17f4e1c1ffc806e9c6cf7f99139.jpg

Right image URL: https://images-na.ssl-images-amazon.com/images/I/51%2BXiF5%2B-5L._SY550_.jpg

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

