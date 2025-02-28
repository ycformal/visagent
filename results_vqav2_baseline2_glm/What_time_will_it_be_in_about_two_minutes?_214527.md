Question: What time will it be in about two minutes?

Reference Answer: 1:00

Image path: ./sampled_GQA/214527.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What time will it be in about two minutes?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What time will it be in about two minutes?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What time will it be in about two minutes?')=<b><span style='color: green;'>1:00</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>1:00</span></b></div><hr>

Answer: 1:00

