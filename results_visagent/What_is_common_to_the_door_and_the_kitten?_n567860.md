Question: What is common to the door and the kitten?

Reference Answer: The color, both the door and the kitten are white.

Image path: ./sampled_GQA/n567860.jpg

Program:

```
 What's in common between A and B?
Program:
ANSWER0=VQA(image=IMAGE,question='What is common to the door and the kitten?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is common to the door and the kitten?')=<b><span style='color: green;'>open</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>open</span></b></div><hr>

Answer: open
