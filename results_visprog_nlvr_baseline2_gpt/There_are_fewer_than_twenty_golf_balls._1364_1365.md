Question: There are fewer than twenty golf balls.

Reference Answer: True

Left image URL: https://ae01.alicdn.com/kf/HTB1nwR4NVXXXXXqXpXXq6xXFXXXf/6pcs-lot-Assorted-Color-Mini-Golf-Balls-Colorful-Golf-Practice-Balls-Training-Golf-Pelotas.jpg_640x640.jpg

Right image URL: https://www.citygolf-uk.com/prodimages/MGA-135_medium.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many golf balls are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} < 20')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many golf balls are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} < 20')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many golf balls are in the image?')=<b><span style='color: green;'>9</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 < 20")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="9 < 20")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

