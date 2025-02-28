Question: Is he frightened?

Reference Answer: yes

Image path: ./sampled_GQA/526576.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Is he frightened?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is he frightened?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

