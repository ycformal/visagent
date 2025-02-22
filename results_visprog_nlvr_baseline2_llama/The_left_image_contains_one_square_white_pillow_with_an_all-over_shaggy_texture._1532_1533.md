Question: The left image contains one square white pillow with an all-over shaggy texture.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/1a/49/61/1a49613e4c8ee2008ee761a6a37df449--gold-pillows-throw-pillows.jpg

Right image URL: https://i.pinimg.com/236x/11/58/5f/11585fc8a75bb96793414194fb4e3403--pillows--throws-cushions.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Does the image contain one square white pillow with an all-over shaggy texture?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Does the image contain one square white pillow with an all-over shaggy texture?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the image contain one square white pillow with an all-over shaggy texture?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

