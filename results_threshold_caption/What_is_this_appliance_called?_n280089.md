Question: What is this appliance called?

Reference Answer: That is a stove.

Image path: ./sampled_GQA/n280089.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is this appliance called?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is this appliance called?')=<b><span style='color: green;'>stove</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>stove</span></b></div><hr>

Answer: stove
