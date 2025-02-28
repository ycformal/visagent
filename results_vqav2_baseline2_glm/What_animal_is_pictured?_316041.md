Question: What animal is pictured?

Reference Answer: cow

Image path: ./sampled_GQA/316041.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What animal is pictured?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What animal is pictured?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What animal is pictured?')=<b><span style='color: green;'>cow</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>cow</span></b></div><hr>

Answer: cow

