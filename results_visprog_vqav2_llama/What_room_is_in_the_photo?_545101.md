Question: What room is in the photo?

Reference Answer: kitchen

Image path: ./sampled_GQA/545101.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What room is in the photo?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What room is in the photo?')=<b><span style='color: green;'>kitchen</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>kitchen</span></b></div><hr>

Answer: kitchen

