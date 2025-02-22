Question: The left image contains one dog standing on snow.

Reference Answer: False

Left image URL: http://4.bp.blogspot.com/-HHD98kGGB7o/Uju1gUdVWFI/AAAAAAAAKdw/v0bWbTCFRgU/s1600/Bethany4.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/23/d4/e4/23d4e4150615dbb995656390e3fe7b47.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many dogs are standing on snow?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)The statement is True.
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many dogs are standing on snow?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)The statement is True.
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many dogs are standing on snow?')=<b><span style='color: green;'>0</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="0 == 1")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

