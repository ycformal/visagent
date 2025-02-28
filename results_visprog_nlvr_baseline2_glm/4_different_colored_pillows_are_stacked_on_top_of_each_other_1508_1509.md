Question: 4 different colored pillows are stacked on top of each other

Reference Answer: True

Left image URL: https://i.pinimg.com/236x/65/35/d8/6535d8f631dd8a18ec33416fc0a8e5a0--beige-color-in-color.jpg

Right image URL: https://i.pinimg.com/236x/f6/b3/54/f6b354dda8713a3f1a020d1f4f8dab76--bright-pillows-accent-pillows.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is '4 different colored pillows are stacked on top of each other' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is '4 different colored pillows are stacked on top of each other' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

