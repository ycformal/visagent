Question: At least 2 regular mittens are stacked on top of each other.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/0e/8c/66/0e8c66f63ca99664a9f14a6de36682d6.jpg

Right image URL: http://knitty.com/ISSUEsummer05/images/manlymittsBEAUTY.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many regular mittens are stacked on top of each other?')
ANSWER1=EVAL(expr='{ANSWER0} >= 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many regular mittens are stacked on top of each other?')
ANSWER1=EVAL(expr='{ANSWER0} >= 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many regular mittens are stacked on top of each other?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 >= 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 >= 2")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

