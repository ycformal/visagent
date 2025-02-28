Question: Does this water look murky?

Reference Answer: no

Image path: ./sampled_GQA/175642.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Does this water look murky?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Does this water look murky?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does this water look murky?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

