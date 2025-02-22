Question: The drawing on the left features a single dog.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/94/f6/5a/94f65a39c83de65e87ce7ebaf3192b94.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/fb/11/17/fb111780675e433d231c5e0d799b0746.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many dogs are in the drawing?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many dogs are in the drawing?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many dogs are in the drawing?')=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="2 == 1")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

