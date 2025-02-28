Question: What color is his tie?

Reference Answer: red

Image path: ./sampled_GQA/125051.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What color is his tie?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What color is his tie?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is his tie?')=<b><span style='color: green;'>red</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>red</span></b></div><hr>

Answer: red

