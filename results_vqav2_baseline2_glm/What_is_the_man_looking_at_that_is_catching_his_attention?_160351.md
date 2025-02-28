Question: What is the man looking at that is catching his attention?

Reference Answer: another skater

Image path: ./sampled_GQA/160351.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What is the man looking at that is catching his attention?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the man looking at that is catching his attention?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the man looking at that is catching his attention?')=<b><span style='color: green;'>ground</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>ground</span></b></div><hr>

Answer: ground

