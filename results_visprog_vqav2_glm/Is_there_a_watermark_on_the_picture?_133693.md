Question: Is there a watermark on the picture?

Reference Answer: no

Image path: ./sampled_GQA/133693.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Is there a watermark on the picture?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a watermark on the picture?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

