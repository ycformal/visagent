Question: Is it an outdoors scene?

Reference Answer: No, it is indoors.

Image path: ./sampled_GQA/n278312.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Is it an outdoors scene?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it an outdoors scene?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
