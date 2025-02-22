Question: There are exactly six cups in the left image.

Reference Answer: True

Left image URL: https://images-na.ssl-images-amazon.com/images/I/71KveSI0P-L._SX355_.jpg

Right image URL: https://i.pinimg.com/736x/12/4c/70/124c7014d16ad88d3eccdeacfc1a0254--material.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many cups are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 6')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many cups are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 6')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many cups are in the image?')=<b><span style='color: green;'>6</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 6")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="6 == 6")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

