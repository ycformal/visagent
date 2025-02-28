Question: Where is the man?

Reference Answer: dorm room

Image path: ./sampled_GQA/329789.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Where is the man?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Where is the man?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Where is the man?')=<b><span style='color: green;'>bedroom</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>bedroom</span></b></div><hr>

Answer: bedroom

