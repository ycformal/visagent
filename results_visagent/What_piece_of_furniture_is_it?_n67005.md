Question: What piece of furniture is it?

Reference Answer: The piece of furniture is a bed.

Image path: ./sampled_GQA/n67005.jpg

Program:

```
 What is A?
Program:
ANSWER0=VQA(image=IMAGE,question='What piece of furniture is it?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What piece of furniture is it?')=<b><span style='color: green;'>bed</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>bed</span></b></div><hr>

Answer: bed
