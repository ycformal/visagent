Question: Was the picture taken at a field or at a beach?

Reference Answer: It was taken at a field.

Image path: ./sampled_GQA/n334278.jpg

Program:

```
 Was A taken at <place> or at <place>?
Program:
ANSWER0=VQA(image=IMAGE,question='Was the picture taken at a field or at a beach?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Was the picture taken at a field or at a beach?')=<b><span style='color: green;'>field</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>field</span></b></div><hr>

Answer: field
