Question: What sport is being played?

Reference Answer: tennis

Image path: ./sampled_GQA/188537.jpg

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

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What sport is being played?')=<b><span style='color: green;'>tennis</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>tennis</span></b></div><hr>

Answer: tennis

