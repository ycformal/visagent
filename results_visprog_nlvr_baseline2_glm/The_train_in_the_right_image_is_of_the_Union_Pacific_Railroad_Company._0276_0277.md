Question: The train in the right image is of the Union Pacific Railroad Company.

Reference Answer: True

Left image URL: http://www.american-rails.com/images/CPRAILMLWM.jpg

Right image URL: http://www.american-rails.com/images/UP855Set.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The train in the right image is of the Union Pacific Railroad Company.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The train in the right image is of the Union Pacific Railroad Company.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

