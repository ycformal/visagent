Question: Each image shows one frontward-facing wolf, but one wolf has its head and gaze turned slightly to the left.

Reference Answer: False

Left image URL: https://i.pinimg.com/236x/c2/1b/d1/c21bd1624221e3561668032b765e9e14--pretty-eyes-wild-dogs.jpg

Right image URL: http://media.oregonlive.com/environment_impact/photo/montanawolfjpg-63ba692820a3a7e6.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image shows one frontward-facing wolf, but one wolf has its head and gaze turned slightly to the left.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image shows one frontward-facing wolf, but one wolf has its head and gaze turned slightly to the left.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

