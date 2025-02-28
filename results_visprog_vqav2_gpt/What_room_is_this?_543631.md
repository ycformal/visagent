Question: What room is this?

Reference Answer: bedroom

Image path: ./sampled_GQA/543631.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What room is this?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What room is this?')=<b><span style='color: green;'>bedroom</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>bedroom</span></b></div><hr>

Answer: bedroom

