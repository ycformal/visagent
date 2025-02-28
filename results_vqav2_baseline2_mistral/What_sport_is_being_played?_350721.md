Question: What sport is being played?

Reference Answer: frisbee

Image path: ./sampled_GQA/350721.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What sport is being played?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What sport is being played?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What sport is being played?')=<b><span style='color: green;'>frisbee</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>frisbee</span></b></div><hr>

Answer: frisbee

