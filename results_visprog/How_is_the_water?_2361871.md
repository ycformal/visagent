Question: How is the water?

Reference Answer: The water is calm.

Image path: ./sampled_GQA/2361871.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='How is the water?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How is the water?')=<b><span style='color: green;'>wavy</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>wavy</span></b></div><hr>

Answer: wavy

