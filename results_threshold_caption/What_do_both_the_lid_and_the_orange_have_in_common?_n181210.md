Question: What do both the lid and the orange have in common?

Reference Answer: The shape, both the lid and the orange are round.

Image path: ./sampled_GQA/n181210.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What do both the lid and the orange have in common?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What do both the lid and the orange have in common?')=<b><span style='color: green;'>they are white</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>they are white</span></b></div><hr>

Answer: "They are white"
