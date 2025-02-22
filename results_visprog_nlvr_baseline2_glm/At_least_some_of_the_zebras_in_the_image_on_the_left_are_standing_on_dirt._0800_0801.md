Question: At least some of the zebras in the image on the left are standing on dirt.

Reference Answer: True

Left image URL: https://nrhatch.files.wordpress.com/2013/01/zebras.jpg

Right image URL: http://2.bp.blogspot.com/-3KKSX08PFDs/TgWziD6W_QI/AAAAAAAAAuA/dlx3BljYM_E/s400/6.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Are some of the zebras standing on dirt?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Are some of the zebras standing on dirt?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are some of the zebras standing on dirt?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

