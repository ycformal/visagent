Question: What is in the mirror?

Reference Answer: school bus

Image path: ./sampled_GQA/291538.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What is in the mirror?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What is in the mirror?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is in the mirror?')=<b><span style='color: green;'>bus</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>bus</span></b></div><hr>

Answer: yellow school bus

