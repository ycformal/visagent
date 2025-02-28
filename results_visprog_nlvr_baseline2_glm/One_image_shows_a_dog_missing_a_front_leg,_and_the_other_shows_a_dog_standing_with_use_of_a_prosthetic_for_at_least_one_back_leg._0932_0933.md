Question: One image shows a dog missing a front leg, and the other shows a dog standing with use of a prosthetic for at least one back leg.

Reference Answer: False

Left image URL: https://i.ytimg.com/vi/VpvACsh-wr8/hqdefault.jpg

Right image URL: https://i.pinimg.com/736x/1a/14/32/1a14322e6435827175df9d401cea799d--dashboards-my-name-is.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a dog missing a front leg, and the other shows a dog standing with use of a prosthetic for at least one back leg.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a dog missing a front leg, and the other shows a dog standing with use of a prosthetic for at least one back leg.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

