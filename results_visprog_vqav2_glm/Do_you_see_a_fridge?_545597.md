Question: Do you see a fridge?

Reference Answer: no

Image path: ./sampled_GQA/545597.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Do you see a fridge?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Do you see a fridge?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

