Question: Does the couch have a different color than the TV?

Reference Answer: no

Image path: ./sampled_GQA/n275148.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='couch')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='tv')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='What color is the couch?')
ANSWER1=VQA(image=IMAGE1,question='What color is the tv?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0}!= {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Does the couch have a different color than the TV?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the couch have a different color than the TV?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

