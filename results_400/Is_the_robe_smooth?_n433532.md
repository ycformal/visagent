Question: Is the robe smooth?

Reference Answer: Yes, the robe is smooth.

Image path: ./sampled_GQA/n433532.jpg

Chain:

```
VQA(Is the robe smooth?)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is the robe smooth?')
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the robe smooth?')=<b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes.
