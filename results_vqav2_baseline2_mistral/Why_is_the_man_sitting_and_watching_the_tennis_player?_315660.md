Question: Why is the man sitting and watching the tennis player?

Reference Answer: watching game

Image path: ./sampled_GQA/315660.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Why is the man sitting and watching the tennis player?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Why is the man sitting and watching the tennis player?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Why is the man sitting and watching the tennis player?')=<b><span style='color: green;'>he's referee</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>he's referee</span></b></div><hr>

Answer: he's referee

