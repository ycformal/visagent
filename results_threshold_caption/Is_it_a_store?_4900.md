Question: Is it a store?

Reference Answer: No, it is an office.

Image path: ./sampled_GQA/4900.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Is it a store?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it a store?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No
