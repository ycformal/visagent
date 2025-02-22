Question: Several boats are in the water in the image on the left.

Reference Answer: False

Left image URL: http://www.advertiser.ie/images/2008/08/1208.jpg

Right image URL: https://maryrussellwriter.files.wordpress.com/2014/06/2014-may-achill-h-boll-fest-yawls-etc-017.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Are there several boats in the water?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Are there several boats in the water?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there several boats in the water?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

