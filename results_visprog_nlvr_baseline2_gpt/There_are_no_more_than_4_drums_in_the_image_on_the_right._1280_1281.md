Question: There are no more than 4 drums in the image on the right.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/ce/66/9b/ce669b8a60aa3b010bf02e418bf86170.jpg

Right image URL: https://i.pinimg.com/736x/fd/47/6a/fd476a3ffbf230cfc8a1afad7e5dd804--double-bass-drum-sets.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many drums are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} <= 4')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many drums are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} <= 4')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many drums are in the image?')=<b><span style='color: green;'>8</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 <= 4")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="8 <= 4")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

