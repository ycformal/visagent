Question: What animal is this?

Reference Answer: polar bear

Image path: ./sampled_GQA/178361.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What animal is this?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What animal is this?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What animal is this?')=<b><span style='color: green;'>polar bear</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>polar bear</span></b></div><hr>

Answer: polar bear

