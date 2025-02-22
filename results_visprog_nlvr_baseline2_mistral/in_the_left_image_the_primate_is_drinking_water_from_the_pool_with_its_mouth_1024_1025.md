Question: in the left image the primate is drinking water from the pool with its mouth

Reference Answer: False

Left image URL: http://www.sapeople.com/wp-content/uploads/2016/03/Hippo.png

Right image URL: https://i.ytimg.com/vi/1cqwd5Y6j9k/maxresdefault.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is the primate drinking water from the pool with its mouth?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Is the primate drinking water from the pool with its mouth?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the primate drinking water from the pool with its mouth?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

