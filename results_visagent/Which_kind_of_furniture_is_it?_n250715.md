Question: Which kind of furniture is it?

Reference Answer: The piece of furniture is a chair.

Image path: ./sampled_GQA/n250715.jpg

Program:

```
 What kind of <category> is A?
Program:
ANSWER0=VQA(image=IMAGE,question='Which kind of furniture is it?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Which kind of furniture is it?')=<b><span style='color: green;'>chair</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>chair</span></b></div><hr>

Answer: chair
