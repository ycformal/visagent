Question: In at least one image there is a saxophone with keys that are a different color from the base instrument.

Reference Answer: False

Left image URL: https://nationalfundforacquisitions.files.wordpress.com/2014/11/alto-saxophone-in-e-flat-c1856.jpg

Right image URL: http://static.musiciansfriend.com/derivates/18/001/238/843/DV016_Jpg_Large_463170.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image there is a saxophone with keys that are a different color from the base instrument.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image there is a saxophone with keys that are a different color from the base instrument.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

