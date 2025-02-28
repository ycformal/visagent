Question: Is the person having fun?

Reference Answer: yes

Image path: ./sampled_GQA/185292.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is the person having fun?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is the person having fun?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the person having fun?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

