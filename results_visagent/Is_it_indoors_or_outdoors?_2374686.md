Question: Is it indoors or outdoors?

Reference Answer: It is outdoors.

Image path: ./sampled_GQA/2374686.jpg

Program:

```
 Is A indoors or outdoors?
Program:
ANSWER0=VQA(image=IMAGE,question='Is it indoors or outdoors?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it indoors or outdoors?')=<b><span style='color: green;'>outdoors</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>outdoors</span></b></div><hr>

Answer: outdoors

