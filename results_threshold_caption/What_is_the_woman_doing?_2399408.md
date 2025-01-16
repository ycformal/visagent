Question: What is the woman doing?

Reference Answer: The woman is running.

Image path: ./sampled_GQA/2399408.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the woman doing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the woman doing?')=<b><span style='color: green;'>running</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>running</span></b></div><hr>

Answer: running

