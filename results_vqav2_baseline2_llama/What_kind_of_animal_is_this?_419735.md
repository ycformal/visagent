Question: What kind of animal is this?

Reference Answer: dog

Image path: ./sampled_GQA/419735.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What kind of animal is this?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What kind of animal is this?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What kind of animal is this?')=<b><span style='color: green;'>dog</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>dog</span></b></div><hr>

Answer: dog

