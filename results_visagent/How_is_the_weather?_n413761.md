Question: How is the weather?

Reference Answer: It is cloudless.

Image path: ./sampled_GQA/n413761.jpg

Program:

```
How is the <attr>?
Program:
ANSWER0=VQA(image=IMAGE,question='How is the weather?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How is the weather?')=<b><span style='color: green;'>clear</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>clear</span></b></div><hr>

Answer: Overcast
