Question: The right image contains at least two ferrets.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/96/63/14/966314c738b9059cab74efc379d90bf7.jpg

Right image URL: https://farm2.staticflickr.com/1017/1186356731_e12e8bb99b_z.jpg?zz=1

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many ferrets are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} >= 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many ferrets are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} >= 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many ferrets are in the image?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 >= 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 >= 2")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

