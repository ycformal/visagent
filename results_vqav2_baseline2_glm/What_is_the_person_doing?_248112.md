Question: What is the person doing?

Reference Answer: playing tennis

Image path: ./sampled_GQA/248112.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What is the person doing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the person doing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the person doing?')=<b><span style='color: green;'>playing tennis</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>playing tennis</span></b></div><hr>

Answer: Playing tennis

