Question: What is this animal called?

Reference Answer: This is an elephant.

Image path: ./sampled_GQA/n544255.jpg

Program:

```
 What is A called?
Program:
ANSWER0=VQA(image=IMAGE,question='What is this animal called?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is this animal called?')=<b><span style='color: green;'>elephant</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>elephant</span></b></div><hr>

Answer: elephant
