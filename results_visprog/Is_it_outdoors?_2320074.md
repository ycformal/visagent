Question: Is it outdoors?

Reference Answer: Yes, it is outdoors.

Image path: ./sampled_GQA/2320074.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Is it outdoors?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it outdoors?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
