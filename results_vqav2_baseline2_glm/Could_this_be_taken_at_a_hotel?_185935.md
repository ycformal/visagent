Question: Could this be taken at a hotel?

Reference Answer: yes

Image path: ./sampled_GQA/185935.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Could this be taken at a hotel?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Could this be taken at a hotel?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Could this be taken at a hotel?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

