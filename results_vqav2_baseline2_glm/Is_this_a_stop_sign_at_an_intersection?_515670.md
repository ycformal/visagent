Question: Is this a stop sign at an intersection?

Reference Answer: no

Image path: ./sampled_GQA/515670.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is this a stop sign at an intersection?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is this a stop sign at an intersection?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is this a stop sign at an intersection?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

