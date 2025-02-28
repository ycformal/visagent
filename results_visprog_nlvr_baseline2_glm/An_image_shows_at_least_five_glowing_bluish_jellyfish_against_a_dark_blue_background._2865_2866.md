Question: An image shows at least five glowing bluish jellyfish against a dark blue background.

Reference Answer: True

Left image URL: https://st.depositphotos.com/1000633/4891/i/450/depositphotos_48910007-stock-photo-beautiful-jellyfish-moving-slowly-in.jpg

Right image URL: https://i.ytimg.com/vi/mxvsSCAUMH4/maxresdefault.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many glowing bluish jellyfish are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} >= 5')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many glowing bluish jellyfish are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} >= 5')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many glowing bluish jellyfish are in the image?')=<b><span style='color: green;'>6</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 >= 5")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="6 >= 5")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

