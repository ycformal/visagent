Question: What type of weather do you see?

Reference Answer: It is cloudy.

Image path: ./sampled_GQA/n289376.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What type of weather do you see?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What type of weather do you see?')=<b><span style='color: green;'>cloudy</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>cloudy</span></b></div><hr>

Answer: overcast
