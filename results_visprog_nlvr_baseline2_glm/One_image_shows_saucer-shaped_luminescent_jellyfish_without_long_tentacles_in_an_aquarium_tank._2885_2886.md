Question: One image shows saucer-shaped luminescent jellyfish without long tentacles in an aquarium tank.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/2KTJ8GAWlEs/hqdefault.jpg

Right image URL: http://reefkeeping.com/issues/2003-01/gt/images/rroverflow3.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows saucer-shaped luminescent jellyfish without long tentacles in an aquarium tank.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows saucer-shaped luminescent jellyfish without long tentacles in an aquarium tank.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

