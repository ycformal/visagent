Question: Is stone used to make the statue?

Reference Answer: no

Image path: ./sampled_GQA/n260521.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is stone used to make the statue?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is stone used to make the statue?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is stone used to make the statue?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

