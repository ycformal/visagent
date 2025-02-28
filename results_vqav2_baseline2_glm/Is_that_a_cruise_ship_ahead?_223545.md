Question: Is that a cruise ship ahead?

Reference Answer: yes

Image path: ./sampled_GQA/223545.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is that a cruise ship ahead?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is that a cruise ship ahead?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is that a cruise ship ahead?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

