Question: The image on the right has no more than three jellyfish.

Reference Answer: True

Left image URL: https://st.depositphotos.com/1000633/4891/i/450/depositphotos_48910007-stock-photo-beautiful-jellyfish-moving-slowly-in.jpg

Right image URL: https://i.ytimg.com/vi/mxvsSCAUMH4/maxresdefault.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many jellyfish are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} <= 3')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many jellyfish are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} <= 3')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many jellyfish are in the image?')=<b><span style='color: green;'>3</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 <= 3")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="3 <= 3")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

