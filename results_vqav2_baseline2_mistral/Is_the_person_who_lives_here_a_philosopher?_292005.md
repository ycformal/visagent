Question: Is the person who lives here a philosopher?

Reference Answer: no

Image path: ./sampled_GQA/292005.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is the person who lives here a philosopher?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is the person who lives here a philosopher?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the person who lives here a philosopher?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

