Question: What brand is on the front of the surfboard?

Reference Answer: rip curl

Image path: ./sampled_GQA/499200.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What brand is on the front of the surfboard?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What brand is on the front of the surfboard?')=<b><span style='color: green;'>nike</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>nike</span></b></div><hr>

Answer: nike

