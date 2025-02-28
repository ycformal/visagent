Question: Is that a nice TV?

Reference Answer: no

Image path: ./sampled_GQA/496525.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Is that a nice TV?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is that a nice TV?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

