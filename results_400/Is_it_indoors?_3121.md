Question: Is it indoors?

Reference Answer: No, it is outdoors.

Image path: ./sampled_GQA/3121.jpg

Chain:

```
VQA(Is it indoors?)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is it indoors?')
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it indoors?')=<b><span style='color: green;'>no</span></b></div><hr>

Answer: no
