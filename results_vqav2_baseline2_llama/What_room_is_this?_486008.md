Question: What room is this?

Reference Answer: bathroom

Image path: ./sampled_GQA/486008.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What room is this?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What room is this?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What room is this?')=<b><span style='color: green;'>bathroom</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>bathroom</span></b></div><hr>

Answer: bathroom

