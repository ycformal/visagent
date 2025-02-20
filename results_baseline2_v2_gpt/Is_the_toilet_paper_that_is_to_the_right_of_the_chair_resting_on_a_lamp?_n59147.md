Question: Is the toilet paper that is to the right of the chair resting on a lamp?

Reference Answer: no

Image path: ./sampled_GQA/n59147.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='chair')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='toilet paper')
IMAGE1=CROP_ON(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='lamp')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is the toilet paper that is to the right of the chair resting on a lamp?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the toilet paper that is to the right of the chair resting on a lamp?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

