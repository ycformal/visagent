Question: Each bottle of wine is sitting on a table.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/736x/97/f8/ae/97f8aec564d457ba330e5bf75bcb9664--nice-body-chilli.jpg

Right image URL: http://www.kristalamb.com/wp-content/uploads/2016/09/Fall1.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each bottle of wine is sitting on a table.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each bottle of wine is sitting on a table.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

