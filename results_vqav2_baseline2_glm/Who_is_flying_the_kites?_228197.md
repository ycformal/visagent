Question: Who is flying the kites?

Reference Answer: man

Image path: ./sampled_GQA/228197.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Who is flying the kites?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Who is flying the kites?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Who is flying the kites?')=<b><span style='color: green;'>man</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>man</span></b></div><hr>

Answer: The person sitting on the bench is flying the kite.

