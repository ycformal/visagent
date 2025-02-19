Question: Is it sunny?

Reference Answer: yes

Image path: ./sampled_GQA/n90944.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='sky')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Is it sunny?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is it sunny?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it sunny?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

