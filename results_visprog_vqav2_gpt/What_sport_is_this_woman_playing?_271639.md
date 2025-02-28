Question: What sport is this woman playing?

Reference Answer: tennis

Image path: ./sampled_GQA/271639.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What sport is this woman playing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What sport is this woman playing?')=<b><span style='color: green;'>tennis</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>tennis</span></b></div><hr>

Answer: tennis

