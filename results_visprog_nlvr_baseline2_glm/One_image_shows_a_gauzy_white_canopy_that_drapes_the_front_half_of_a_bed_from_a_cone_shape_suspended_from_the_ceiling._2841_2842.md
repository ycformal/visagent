Question: One image shows a gauzy white canopy that drapes the front half of a bed from a cone shape suspended from the ceiling.

Reference Answer: True

Left image URL: https://vandytang.files.wordpress.com/2016/03/img_9082.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/25/79/b6/2579b6ef1491684ec2ac26a5773d3ba9.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is there a gauzy white canopy that drapes the front half of a bed from a cone shape suspended from the ceiling?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Is there a gauzy white canopy that drapes the front half of a bed from a cone shape suspended from the ceiling?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a gauzy white canopy that drapes the front half of a bed from a cone shape suspended from the ceiling?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

