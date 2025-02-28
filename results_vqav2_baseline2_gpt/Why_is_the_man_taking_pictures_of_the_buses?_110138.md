Question: Why is the man taking pictures of the buses?

Reference Answer: picture

Image path: ./sampled_GQA/110138.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Why is the man taking pictures of the buses?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Why is the man taking pictures of the buses?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Why is the man taking pictures of the buses?')=<b><span style='color: green;'>for fun</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>for fun</span></b></div><hr>

Answer: for fun

