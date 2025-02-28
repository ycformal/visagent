Question: In at least one image there are four stories and each roof is painted with goal and topped with a gold circle.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/EfhvwSGpYP4/maxresdefault.jpg

Right image URL: https://1.bp.blogspot.com/-ztlJ430spL0/WZLAb3Ef35I/AAAAAAAABqU/sE5FmL4wLq4aKsb47BFFWFo0bEUy2v2zACLcBGAs/s1600/Namdroling-Monastery-Golden-Temple-Bylakuppe-coorg-Karnataka-south-India-Travel_6.JPG

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
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image there are four stories and each roof is painted with goal and topped with a gold circle.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image there are four stories and each roof is painted with goal and topped with a gold circle.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

