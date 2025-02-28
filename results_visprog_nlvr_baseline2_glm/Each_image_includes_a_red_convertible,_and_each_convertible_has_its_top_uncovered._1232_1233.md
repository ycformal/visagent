Question: Each image includes a red convertible, and each convertible has its top uncovered.

Reference Answer: True

Left image URL: https://pbs.twimg.com/media/DBQmHhDXYAET7Gs.jpg

Right image URL: http://pop.h-cdn.co/assets/cm/15/05/54cb1d27e3132_-_analog-sports-cars-02-1013-de.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image includes a red convertible, and each convertible has its top uncovered.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image includes a red convertible, and each convertible has its top uncovered.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

