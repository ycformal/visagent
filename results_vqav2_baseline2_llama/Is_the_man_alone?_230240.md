Question: Is the man alone?

Reference Answer: no

Image path: ./sampled_GQA/230240.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='man')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 1 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is the man alone?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the man alone?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

