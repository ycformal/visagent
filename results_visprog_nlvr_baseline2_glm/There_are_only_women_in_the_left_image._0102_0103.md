Question: There are only women in the left image.

Reference Answer: False

Left image URL: https://marketplace.canva.com/MABFbtcFgCQ/1/screen/canva-fitness-people-working-out-using-dumbbells--MABFbtcFgCQ.jpg

Right image URL: https://st.depositphotos.com/1017986/4056/i/950/depositphotos_40563697-stock-photo-group-of-people-working-out.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are only women in the left image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are only women in the left image.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

