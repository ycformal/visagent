Question: What do both the building and the calf have in common?

Reference Answer: The color, both the building and the calf are white.

Image path: ./sampled_GQA/n331357.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What do the building and the calf have in common?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What do the building and the calf have in common?')=<b><span style='color: green;'>color</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>color</span></b></div><hr>

Answer: color
