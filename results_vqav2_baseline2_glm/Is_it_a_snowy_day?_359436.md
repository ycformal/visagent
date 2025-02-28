Question: Is it a snowy day?

Reference Answer: no

Image path: ./sampled_GQA/359436.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is it a snowy day?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is it a snowy day?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it a snowy day?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

