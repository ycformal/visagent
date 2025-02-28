Question: Which vegetable is kept on the chopper board?

Reference Answer: carrot

Image path: ./sampled_GQA/381413.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Which vegetable is kept on the chopper board?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Which vegetable is kept on the chopper board?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Which vegetable is kept on the chopper board?')=<b><span style='color: green;'>carrot</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>carrot</span></b></div><hr>

Answer: carrot

