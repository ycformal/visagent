Question: The right image shows a row of standing bikini models with at least one model's rear turned to the camera.

Reference Answer: True

Left image URL: http://hollywoodpq.com/wp-content/uploads/2015/07/224-e1437162424167.jpg

Right image URL: http://y3.ifengimg.com/a/2014_46/51aaecf08cd52c3.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Are there at least one model\'s rear turned to the camera?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Are there at least one model\'s rear turned to the camera?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there at least one model's rear turned to the camera?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

