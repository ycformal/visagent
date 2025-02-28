Question: One image shows a pair of round-topped drums that sit upright without stands and taper from top to bottom, and the other image shows two more cylindrical, squat drums that have small feet.

Reference Answer: True

Left image URL: https://cdn.shopclues.com/images/thumbnails/42420/320/320/HolyKrishnasProfessionalLongLastingTwoPieceBongoDrumsetFreeTwoProfessionalDrumStickB01I9JRB6Y1470662285.jpg

Right image URL: http://images.wisegeek.com/hands-playing-bongos.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a pair of round-topped drums that sit upright without stands and taper from top to bottom, and the other image shows two more cylindrical, squat drums that have small feet.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a pair of round-topped drums that sit upright without stands and taper from top to bottom, and the other image shows two more cylindrical, squat drums that have small feet.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

