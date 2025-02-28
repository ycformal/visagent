Question: Which room is this?

Reference Answer: kitchen

Image path: ./sampled_GQA/543525.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Which room is this?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Which room is this?')=<b><span style='color: green;'>kitchen</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>kitchen</span></b></div><hr>

Answer: kitchen

