Question: What is common to the sculpture and the fireplace?

Reference Answer: The color, both the sculpture and the fireplace are black.

Image path: ./sampled_GQA/n23181.jpg

Program:

```
What is common between A and B?
Program:
ANSWER0=VQA(image=IMAGE,question='What is common to the sculpture and the fireplace?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is common to the sculpture and the fireplace?')=<b><span style='color: green;'>they are both white</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>they are both white</span></b></div><hr>

Answer: they are both white

