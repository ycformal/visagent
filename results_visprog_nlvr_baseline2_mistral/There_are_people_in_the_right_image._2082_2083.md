Question: There are people in the right image.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/c8/26/a8/c826a8c9ccfecaa5b99ecfbbcc587dda--the-barber-barber-shop.jpg

Right image URL: https://s.hdnux.com/photos/34/34/20/7455744/3/920x920.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Are there people in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Are there people in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there people in the image?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

