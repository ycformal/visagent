Question: Is this person packing or unpacking?

Reference Answer: packing

Image path: ./sampled_GQA/85637.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is this person packing or unpacking?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is this person packing or unpacking?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is this person packing or unpacking?')=<b><span style='color: green;'>packing</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>packing</span></b></div><hr>

Answer: packing

