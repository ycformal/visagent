Question: the right pic has the dogs mouth open

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/736x/e5/a9/f3/e5a9f3d0e5daf51bfa7b7289d654581d--russian-wolfhound-afghan.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/8e/e3/d9/8ee3d9786d7f8cb15059680dc98970b5.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is the dog's mouth open?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is the dog's mouth open?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the dog')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

