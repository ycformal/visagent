Question: How is the weather in this scene?

Reference Answer: It is cloudy.

Image path: ./sampled_GQA/n489699.jpg

Program:

```
How is the <attr> in this scene?
Program:
ANSWER0=VQA(image=IMAGE,question='How is the weather in this scene?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How is the weather in this scene?')=<b><span style='color: green;'>cold</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>cold</span></b></div><hr>

Answer: cold
