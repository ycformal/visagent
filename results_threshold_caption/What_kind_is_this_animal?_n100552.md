Question: What kind is this animal?

Reference Answer: That is an elephant.

Image path: ./sampled_GQA/n100552.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What kind is this animal?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What kind is this animal?')=<b><span style='color: green;'>elephant</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>elephant</span></b></div><hr>

Answer: elephant
