Question: One elephant has long tusks.

Reference Answer: False

Left image URL: https://pbs.twimg.com/media/BrKJGrQIAAAjIyC.jpg

Right image URL: http://4.bp.blogspot.com/-Xx7Wz7_nHxY/Tpep94dOc8I/AAAAAAAAE9o/CmsNz_8ez18/s1600/sleepingelephant.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One elephant has long tusks.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One elephant has long tusks.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

