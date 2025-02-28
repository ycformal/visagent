Question: Is he playing a game?

Reference Answer: no

Image path: ./sampled_GQA/122549.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Is he playing a game?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is he playing a game?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

