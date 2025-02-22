Question: The train in the right image is of the Union Pacific Railroad Company.

Reference Answer: True

Left image URL: http://www.american-rails.com/images/CPRAILMLWM.jpg

Right image URL: http://www.american-rails.com/images/UP855Set.jpg

Program:

```
ANSWER0=VQA(image=RIGHT,question='Is the train of the Union Pacific Railroad Company?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the train of the Union Pacific Railroad Company?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

