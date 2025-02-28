Question: There is a stairway with an arched doorway under the stairs

Reference Answer: False

Left image URL: https://scotiastairs.com/photos/gallery9/traditional-white-balusters-birch-treads-5.jpg

Right image URL: https://i.pinimg.com/736x/b1/7f/90/b17f90419aa06f905af251672a5ae196--foyers-staircases.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There is a stairway with an arched doorway under the stairs' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a stairway with an arched doorway under the stairs' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

