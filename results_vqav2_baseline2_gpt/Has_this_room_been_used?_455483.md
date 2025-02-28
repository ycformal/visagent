Question: Has this room been used?

Reference Answer: yes

Image path: ./sampled_GQA/455483.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Has this room been used?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Has this room been used?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Has this room been used?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

