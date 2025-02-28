Question: How deep is the water?

Reference Answer: 4 ft

Image path: ./sampled_GQA/331097.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='How deep is the water?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How deep is the water?')=<b><span style='color: green;'>shallow</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>shallow</span></b></div><hr>

Answer: shallow

