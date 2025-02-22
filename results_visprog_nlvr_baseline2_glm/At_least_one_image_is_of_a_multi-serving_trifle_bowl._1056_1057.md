Question: At least one image is of a multi-serving trifle bowl.

Reference Answer: True

Left image URL: http://del.h-cdn.co/assets/16/49/768x432/gallery-1481211452-delish-cookie-trifle-scoop.jpg

Right image URL: https://itsrainingflour.com/wp-content/uploads/2015/12/triflethumbnail.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

