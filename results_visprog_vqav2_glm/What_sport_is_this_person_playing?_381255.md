Question: What sport is this person playing?

Reference Answer: tennis

Image path: ./sampled_GQA/381255.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What sport is this person playing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What sport is this person playing?')=<b><span style='color: green;'>tennis</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>tennis</span></b></div><hr>

Answer: tennis

