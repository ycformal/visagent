Question: Is it indoors or outdoors?

Reference Answer: It is outdoors.

Image path: ./sampled_GQA/2409538.jpg

Chain:

```
VQA(Is it indoors or outdoors?)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is it indoors or outdoors?')
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it indoors or outdoors?')=<b><span style='color: green;'>outdoors</span></b></div><hr>

Answer: outdoors
