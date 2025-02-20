Question: Is there a plate or a can that is made of metal?

Reference Answer: no

Image path: ./sampled_GQA/n166008.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='plate')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Is the plate made of metal?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'yes' else 'no'")
BOX1=LOC(image=IMAGE,object='can')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER2=VQA(image=IMAGE1,question='Is the can made of metal?')
ANSWER3=EVAL(expr="'yes' if {ANSWER2} == 'yes' else 'no'")
ANSWER4=EVAL(expr="'yes' if {ANSWER1} == 'yes' or {ANSWER3} == 'yes' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER4)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is there a plate or a can that is made of metal?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a plate or a can that is made of metal?')=<b><span style='color: green;'>plate</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>plate</span></b></div><hr>

Answer: plate

