Question: In at least one image there is a flag and flagpole in front of a monastery

Reference Answer: True

Left image URL: https://www.trekkinginsikkim.com/images/sikkim-monastery-tour4.jpg

Right image URL: https://i0.wp.com/www.placeforvacations.com/wp-content/uploads/2014/08/Phensang-Monastery-Famous-monastery-of-Sikkim.jpg?fit=810%2C608&ssl=1

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
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image there is a flag and flagpole in front of a monastery' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image there is a flag and flagpole in front of a monastery' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

