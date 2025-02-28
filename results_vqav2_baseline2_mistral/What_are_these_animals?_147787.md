Question: What are these animals?

Reference Answer: dogs

Image path: ./sampled_GQA/147787.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What are these animals?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What are these animals?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What are these animals?')=<b><span style='color: green;'>dogs</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>dogs</span></b></div><hr>

Answer: dogs

