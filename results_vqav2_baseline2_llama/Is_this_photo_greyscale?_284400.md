Question: Is this photo greyscale?

Reference Answer: no

Image path: ./sampled_GQA/284400.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is this photo greyscale?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is this photo greyscale?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is this photo greyscale?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

