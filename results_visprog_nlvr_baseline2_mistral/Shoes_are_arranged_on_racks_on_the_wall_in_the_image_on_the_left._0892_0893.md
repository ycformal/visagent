Question: Shoes are arranged on racks on the wall in the image on the left.

Reference Answer: False

Left image URL: https://cdn.runblogger.com/images/2014/01/new-balance-890v4-sole.jpg

Right image URL: https://s3-media3.fl.yelpcdn.com/bphoto/yUWrSQqan7gzqLUwIMfygw/ls.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Are shoes arranged on racks on the wall?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Are shoes arranged on racks on the wall?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are shoes arranged on racks on the wall?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

