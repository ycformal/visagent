Question: the right pic has the dogs mouth open

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/2d/31/08/2d31086b37de9f484187868eb137212f--russian-wolfhound-greyhound.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/736x/a0/9d/14/a09d14ac9626983bfe3eb00dfa402bda.jpg

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

