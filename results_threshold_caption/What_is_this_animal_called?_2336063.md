Question: What is this animal called?

Reference Answer: This is a cat.

Image path: ./sampled_GQA/2336063.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is this animal called?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is this animal called?')=<b><span style='color: green;'>cat</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>cat</span></b></div><hr>

Answer: cat
