Question: Was the image taken at the zoo?

Reference Answer: No, the picture was taken in the forest.

Image path: ./sampled_GQA/2328785.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Was the image taken at the zoo?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Was the image taken at the zoo?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
