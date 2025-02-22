Question: The train in the right image is of the Union Pacific Railroad Company.

Reference Answer: True

Left image URL: https://vignette1.wikia.nocookie.net/locomotive/images/4/42/UP_ALCO_C-630.jpg/revision/latest?cb=20110804021442

Right image URL: https://i.pinimg.com/736x/47/8d/76/478d76399f4fd2369c8456ecff41dc6b--diesel-locomotive-train-travel.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is the train in the image from the Union Pacific Railroad Company?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is the train in the image from the Union Pacific Railroad Company?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the train in the image from the Union Pacific Railroad Company?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

