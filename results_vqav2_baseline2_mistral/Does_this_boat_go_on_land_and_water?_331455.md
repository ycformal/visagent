Question: Does this boat go on land and water?

Reference Answer: no

Image path: ./sampled_GQA/331455.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Does this boat go on land and water?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Does this boat go on land and water?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does this boat go on land and water?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

