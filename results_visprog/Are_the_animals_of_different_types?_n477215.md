Question: Are the animals of different types?

Reference Answer: No, all the animals are birds.

Image path: ./sampled_GQA/n477215.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Are the animals of different types?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are the animals of different types?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

