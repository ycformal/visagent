Question: The left and right image contains the same number of fully white canopies.

Reference Answer: True

Left image URL: https://i.pinimg.com/originals/d9/f3/f9/d9f3f91d4e2f281a8825a20adb2b20df.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/236x/1d/c8/24/1dc824722246b1684609b16f91871f08.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains the same number of fully white canopies.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains the same number of fully white canopies.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

