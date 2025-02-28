Question: What room is this?

Reference Answer: bathroom

Image path: ./sampled_GQA/156832.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What room is this?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What room is this?')=<b><span style='color: green;'>bathroom</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>bathroom</span></b></div><hr>

Answer: bathroom

