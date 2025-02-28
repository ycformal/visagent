Question: Why is there so much smoke on the train?

Reference Answer: wood burning

Image path: ./sampled_GQA/39790.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Why is there so much smoke on the train?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Why is there so much smoke on the train?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Why is there so much smoke on the train?')=<b><span style='color: green;'>engine</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>engine</span></b></div><hr>

Answer: engine

