Question: What sport is being played?

Reference Answer: baseball

Image path: ./sampled_GQA/223243.jpg

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

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What sport is being played?')=<b><span style='color: green;'>baseball</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>baseball</span></b></div><hr>

Answer: baseball

