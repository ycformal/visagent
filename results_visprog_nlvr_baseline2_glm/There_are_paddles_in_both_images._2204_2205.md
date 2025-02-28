Question: There are paddles in both images.

Reference Answer: True

Left image URL: https://i.pinimg.com/originals/1f/80/ae/1f80ae222e327d61aa39478fbb45fe78.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/31/1f/a9/311fa9ce3eb65ff10215a84207f88088.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are paddles in both images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are paddles in both images.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

