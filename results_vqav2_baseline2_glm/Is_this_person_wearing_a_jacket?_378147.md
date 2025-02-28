Question: Is this person wearing a jacket?

Reference Answer: yes

Image path: ./sampled_GQA/378147.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is this person wearing a jacket?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is this person wearing a jacket?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is this person wearing a jacket?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

