Question: There three fishes in total swimming near an anemone.

Reference Answer: True

Left image URL: https://seaunseen.com/wp-content/uploads/2014/11/Skunk-Clown-3-swm.jpg

Right image URL: https://images.robertharding.com/preview/RM/RH/HORIZONTAL/1159-286.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There three fishes in total swimming near an anemone.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There three fishes in total swimming near an anemone.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

