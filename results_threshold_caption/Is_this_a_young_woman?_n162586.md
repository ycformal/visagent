Question: Is this a young woman?

Reference Answer: Yes, this is a young woman.

Image path: ./sampled_GQA/n162586.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Is this a young woman?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is this a young woman?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
