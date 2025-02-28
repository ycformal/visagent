Question: A beetle on top of a dungball is facing left.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/-MMfqh-QbGY/hqdefault.jpg

Right image URL: https://render.fineartamerica.com/images/rendered/search/canvas-print/mirror/break/images-medium-5/2-dung-beetle-f-martinez-clavel-canvas-print.jpg

Original program:

```
Statement: A beetle on top of a dungball is facing left.
Program:
ANSWER0=VQA(image=LEFT,question='Is there a beetle on top of a dungball?')
ANSWER1=VQA(image=RIGHT,question='Is there a beetle on top of a dungball?')
ANSWER2=VQA(image=LEFT,question='Is the beetle facing left?')
ANSWER3=VQA(image=RIGHT,question='Is the beetle facing left?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A beetle on top of a dungball is facing left.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A beetle on top of a dungball is facing left.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

