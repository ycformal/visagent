Question: Which place is it?

Reference Answer: It is a field.

Image path: ./sampled_GQA/2356423.jpg

Program:

```
Complex question (place, weather, etc.)
Program:
ANSWER0=VQA(image=IMAGE,question='Which place is it?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Which place is it?')=<b><span style='color: green;'>baseball field</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>baseball field</span></b></div><hr>

Answer: baseball field

