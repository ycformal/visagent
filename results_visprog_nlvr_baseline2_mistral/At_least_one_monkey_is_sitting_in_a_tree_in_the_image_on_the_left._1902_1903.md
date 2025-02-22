Question: At least one monkey is sitting in a tree in the image on the left.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/bf/13/b8/bf13b876dffacd287132a513caf77aee.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/20/ef/02/20ef023bec5fb7b4135db2ea6c0d4f5b.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many monkeys are sitting in a tree?')
ANSWER1=EVAL(expr='{ANSWER0} >= 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many monkeys are sitting in a tree?')
ANSWER1=EVAL(expr='{ANSWER0} >= 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many monkeys are sitting in a tree?')=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 >= 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="2 >= 1")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

