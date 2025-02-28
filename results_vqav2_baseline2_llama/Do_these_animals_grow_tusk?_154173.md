Question: Do these animals grow tusk?

Reference Answer: yes

Image path: ./sampled_GQA/154173.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Do these animals grow tusk?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Do these animals grow tusk?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Do these animals grow tusk?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

