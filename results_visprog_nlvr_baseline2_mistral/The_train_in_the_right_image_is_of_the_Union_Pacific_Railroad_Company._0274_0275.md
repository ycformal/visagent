Question: The train in the right image is of the Union Pacific Railroad Company.

Reference Answer: False

Left image URL: http://canadianrailwayobservations.com/RESTRICTED/2016/August2016/images/south/up5033tomchenoweth.jpg

Right image URL: https://media-cdn.tripadvisor.com/media/photo-s/01/99/4c/f2/santa-fe-diesel.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is the train of the Union Pacific Railroad Company?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is the train of the Union Pacific Railroad Company?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the train of the Union Pacific Railroad Company?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

