Question: One image contains a single puppy, and the other image contains a horizontal row of four spaniels with similar poses but varied fur colors.

Reference Answer: True

Left image URL: https://78.media.tumblr.com/d6ceb229d827660372f98c608caecbe0/tumblr_ov3halpGNj1t1cy7no1_500.jpg

Right image URL: http://static.tumblr.com/dxmlptq/CBEm71ywb/startfoto.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image contains a single puppy, and the other image contains a horizontal row of four spaniels with similar poses but varied fur colors.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image contains a single puppy, and the other image contains a horizontal row of four spaniels with similar poses but varied fur colors.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

