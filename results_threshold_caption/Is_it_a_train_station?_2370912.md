Question: Is it a train station?

Reference Answer: Yes, it is a train station.

Image path: ./sampled_GQA/2370912.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Is it a train station?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it a train station?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

