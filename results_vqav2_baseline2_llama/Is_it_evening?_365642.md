Question: Is it evening?

Reference Answer: yes

Image path: ./sampled_GQA/365642.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is it evening?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is it evening?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it evening?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

