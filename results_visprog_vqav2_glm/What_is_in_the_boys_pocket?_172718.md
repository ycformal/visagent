Question: What is in the boys pocket?

Reference Answer: pen

Image path: ./sampled_GQA/172718.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is in the boys pocket?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is in the boys pocket?')=<b><span style='color: green;'>pen</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>pen</span></b></div><hr>

Answer: pen

