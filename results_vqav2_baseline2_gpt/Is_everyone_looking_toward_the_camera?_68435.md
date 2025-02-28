Question: Is everyone looking toward the camera?

Reference Answer: no

Image path: ./sampled_GQA/68435.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='camera')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is everyone looking toward the camera?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is everyone looking toward the camera?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

