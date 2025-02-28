Question: What is this person doing?

Reference Answer: swinging bat

Image path: ./sampled_GQA/80429.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What is this person doing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What is this person doing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is this person doing?')=<b><span style='color: green;'>batting</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>batting</span></b></div><hr>

Answer: batting

