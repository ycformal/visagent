Question: Is this man in a competition?

Reference Answer: no

Image path: ./sampled_GQA/365099.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Is this man in a competition?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is this man in a competition?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

