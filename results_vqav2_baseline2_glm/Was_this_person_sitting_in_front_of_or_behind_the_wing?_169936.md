Question: Was this person sitting in front of or behind the wing?

Reference Answer: behind

Image path: ./sampled_GQA/169936.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='wing')
IMAGE0=CROP_ABOVE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'behind' if {ANSWER0} > 0 else 'in front of'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Was this person sitting in front of or behind the wing?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Was this person sitting in front of or behind the wing?')=<b><span style='color: green;'>front</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>front</span></b></div><hr>

Answer: front

