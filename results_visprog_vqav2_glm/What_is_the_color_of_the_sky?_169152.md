Question: What is the color of the sky?

Reference Answer: blue

Image path: ./sampled_GQA/169152.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the color of the sky?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the color of the sky?')=<b><span style='color: green;'>blue</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>blue</span></b></div><hr>

Answer: blue

