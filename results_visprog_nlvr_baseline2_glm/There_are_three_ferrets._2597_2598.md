Question: There are three ferrets.

Reference Answer: True

Left image URL: http://schmoopac.tripod.com/images/chocolate.jpg

Right image URL: https://i.pinimg.com/236x/85/c5/6c/85c56cc8cc36cd58e9696930ba242759--small-animals-wild-animals.jpg

Original program:

```
Statement: There are three ferrets.
Program:
ANSWER0=VQA(image=LEFT,question='How many ferrets are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many ferrets are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} == 3')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are three ferrets.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are three ferrets.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

