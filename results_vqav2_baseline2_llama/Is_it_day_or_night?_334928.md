Question: Is it day or night?

Reference Answer: day

Image path: ./sampled_GQA/334928.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is it day or night?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is it day or night?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it day or night?')=<b><span style='color: green;'>day</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>day</span></b></div><hr>

Answer: day

