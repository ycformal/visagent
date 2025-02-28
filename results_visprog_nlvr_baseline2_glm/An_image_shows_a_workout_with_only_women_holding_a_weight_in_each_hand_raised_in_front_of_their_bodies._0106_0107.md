Question: An image shows a workout with only women holding a weight in each hand raised in front of their bodies.

Reference Answer: True

Left image URL: https://st2.depositphotos.com/1017986/6067/i/950/depositphotos_60676481-stock-photo-group-of-women-with-dumbbells.jpg

Right image URL: https://st2.depositphotos.com/1017986/7792/i/950/depositphotos_77926736-stock-photo-group-of-men-with-dumbbells.jpg

Original program:

```
Statement: An image shows a workout with only women holding a weight in each hand raised in front of their bodies.
Program:
ANSWER0=VQA(image=LEFT,question='Is there a workout with only women holding a weight in each hand raised in front of their bodies?')
ANSWER1=VQA(image=RIGHT,question='Is there a workout with only women holding a weight in each hand raised in front of their bodies?')
ANSWER2=EVAL(expr='{ANSWER0} and {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows a workout with only women holding a weight in each hand raised in front of their bodies.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows a workout with only women holding a weight in each hand raised in front of their bodies.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

