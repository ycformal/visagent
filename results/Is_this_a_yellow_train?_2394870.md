Question: Is this a yellow train?

Reference Answer: No, this is a blue train.

Image path: ./sampled_GQA/2394870.jpg

Chain:

```
VQA(Is this a yellow train?)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is this a yellow train?')
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is this a yellow train?')=<b><span style='color: green;'>no</span></b></div><hr>

Answer: No

