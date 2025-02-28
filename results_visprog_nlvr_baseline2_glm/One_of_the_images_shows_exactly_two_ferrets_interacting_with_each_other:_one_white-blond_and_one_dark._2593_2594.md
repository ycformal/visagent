Question: One of the images shows exactly two ferrets interacting with each other: one white/blond and one dark.

Reference Answer: False

Left image URL: https://i.ytimg.com/vi/FGuM8YkY0lE/maxresdefault.jpg

Right image URL: http://1.bp.blogspot.com/-xxTUbcQK9ao/Vi0zIXVZO5I/AAAAAAAAA9Q/63qDr4obkE0/s1600/FullSizeRender%2B%25288%2529.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One of the images shows exactly two ferrets interacting with each other: one white/blond and one dark.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One of the images shows exactly two ferrets interacting with each other: one white/blond and one dark.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

