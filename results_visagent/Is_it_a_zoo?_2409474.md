Question: Is it a zoo?

Reference Answer: No, it is a park.

Image path: ./sampled_GQA/2409474.jpg

Program:

```
Is it A?
Program:
ANSWER0=VQA(image=IMAGE,question='Is it a zoo?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it a zoo?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

