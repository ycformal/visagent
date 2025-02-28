Question: What is the color of the light?

Reference Answer: red

Image path: ./sampled_GQA/287967.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the color of the light?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the color of the light?')=<b><span style='color: green;'>red</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>red</span></b></div><hr>

Answer: red

