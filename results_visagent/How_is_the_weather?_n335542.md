Question: How is the weather?

Reference Answer: It is partly cloudy.

Image path: ./sampled_GQA/n335542.jpg

Program:

```
How is A?
Program:
ANSWER0=VQA(image=IMAGE,question='How is the weather?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How is the weather?')=<b><span style='color: green;'>cloudy</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>cloudy</span></b></div><hr>

Answer: Cloudy
