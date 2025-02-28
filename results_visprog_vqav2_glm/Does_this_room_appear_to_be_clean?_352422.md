Question: Does this room appear to be clean?

Reference Answer: no

Image path: ./sampled_GQA/352422.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Does this room appear to be clean?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does this room appear to be clean?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

