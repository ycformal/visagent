Question: What is the girl doing?

Reference Answer: The girl is standing.

Image path: ./sampled_GQA/2410065.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the girl doing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the girl doing?')=<b><span style='color: green;'>posing</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>posing</span></b></div><hr>

Answer: posing
