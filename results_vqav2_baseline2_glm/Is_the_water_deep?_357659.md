Question: Is the water deep?

Reference Answer: yes

Image path: ./sampled_GQA/357659.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is the water deep?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is the water deep?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the water deep?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

