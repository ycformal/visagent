Question: Each image contains at least one inflated balloon, but the lefthand image contains a greater number of inflated balloons.

Reference Answer: False

Left image URL: https://4.bp.blogspot.com/-xj5dSJfEZkE/VwoK5H2JJlI/AAAAAAAADZ0/oqVe49ZLhCgnW_UMVoiWrg4XDU-GFyPgg/s1600/water%2Bballoon%2B1.jpg

Right image URL: https://potreby-kancelarske.eu/balonek-20012-metaliza~nahled.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains at least one inflated balloon, but the lefthand image contains a greater number of inflated balloons.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains at least one inflated balloon, but the lefthand image contains a greater number of inflated balloons.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

