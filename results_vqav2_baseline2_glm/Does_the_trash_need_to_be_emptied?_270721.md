Question: Does the trash need to be emptied?

Reference Answer: no

Image path: ./sampled_GQA/270721.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Does the trash need to be emptied?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Does the trash need to be emptied?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the trash need to be emptied?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

