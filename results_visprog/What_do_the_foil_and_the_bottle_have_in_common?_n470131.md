Question: What do the foil and the bottle have in common?

Reference Answer: The shape, both the foil and the bottle are round.

Image path: ./sampled_GQA/n470131.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What do the foil and the bottle have in common?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What do the foil and the bottle have in common?')=<b><span style='color: green;'>they are green</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>they are green</span></b></div><hr>

Answer: they are green
