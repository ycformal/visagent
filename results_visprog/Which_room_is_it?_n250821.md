Question: Which room is it?

Reference Answer: It is a bedroom.

Image path: ./sampled_GQA/n250821.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Which room is it?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Which room is it?')=<b><span style='color: green;'>bedroom</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>bedroom</span></b></div><hr>

Answer: bedroom
