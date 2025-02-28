Question: How fast is this woman moving?

Reference Answer: slow

Image path: ./sampled_GQA/446850.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='How fast is this woman moving?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='How fast is this woman moving?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How fast is this woman moving?')=<b><span style='color: green;'>slow</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>slow</span></b></div><hr>

Answer: slow

