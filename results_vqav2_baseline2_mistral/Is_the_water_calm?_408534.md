Question: Is the water calm?

Reference Answer: no

Image path: ./sampled_GQA/408534.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is the water calm?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is the water calm?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the water calm?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

