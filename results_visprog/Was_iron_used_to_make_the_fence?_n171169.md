Question: Was iron used to make the fence?

Reference Answer: No, the fence is made of wire.

Image path: ./sampled_GQA/n171169.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Was iron used to make the fence?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Was iron used to make the fence?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
