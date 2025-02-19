Question: Is there a open window or door?

Reference Answer: no

Image path: ./sampled_GQA/n305495.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='window')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='open')
ANSWER0=COUNT(box=BOX1)
BOX2=LOC(image=IMAGE,object='door')
IMAGE1=CROP(image=IMAGE,box=BOX2)
BOX3=LOC(image=IMAGE1,object='open')
ANSWER1=COUNT(box=BOX3)
ANSWER2=EVAL(expr="'yes' if {ANSWER0} > 0 or {ANSWER1} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is there a open window or door?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a open window or door?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

