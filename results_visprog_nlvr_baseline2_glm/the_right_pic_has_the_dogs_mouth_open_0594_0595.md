Question: the right pic has the dogs mouth open

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/2d/31/08/2d31086b37de9f484187868eb137212f--russian-wolfhound-greyhound.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/736x/a0/9d/14/a09d14ac9626983bfe3eb00dfa402bda.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

