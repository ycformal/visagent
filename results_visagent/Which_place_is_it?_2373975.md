Question: Which place is it?

Reference Answer: It is a highway.

Image path: ./sampled_GQA/2373975.jpg

Program:

```
 Complex question (place, weather, etc.)
Program:
ANSWER0=VQA(image=IMAGE,question='Which place is it?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Which place is it?')=<b><span style='color: green;'>highway</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>highway</span></b></div><hr>

Answer: highway

