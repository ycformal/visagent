Question: Do the cars facing the light have the right of way?

Reference Answer: yes

Image path: ./sampled_GQA/246717.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='light')
IMAGE0=CROP_FACING(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='cars')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Do the cars facing the light have the right of way?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Do the cars facing the light have the right of way?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes.

