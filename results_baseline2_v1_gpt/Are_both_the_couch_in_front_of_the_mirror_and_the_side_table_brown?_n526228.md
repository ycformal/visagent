Question: Are both the couch in front of the mirror and the side table brown?

Reference Answer: yes

Image path: ./sampled_GQA/n526228.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='couch')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='mirror')
IMAGE1=CROP_BEHIND(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE,object='side table')
IMAGE2=CROP_FRONT(image=IMAGE,box=BOX2)
ANSWER0=VQA(image=IMAGE1,question='What color is the couch?')
ANSWER1=VQA(image=IMAGE2,question='What color is the side table?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'brown' and {ANSWER1} == 'brown' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Are both the couch in front of the mirror and the side table brown?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are both the couch in front of the mirror and the side table brown?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

