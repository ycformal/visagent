Question: Do these animals all have the same type?

Reference Answer: no

Image path: ./sampled_GQA/n469525.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Do these animals all have the same type?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Do these animals all have the same type?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Do these animals all have the same type?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

