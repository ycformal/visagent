Question: Are there either white cabinets or beds?

Reference Answer: no

Image path: ./sampled_GQA/n499081.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='cabinets')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='white')
ANSWER0=COUNT(box=BOX1)
BOX2=LOC(image=IMAGE,object='bed')
IMAGE1=CROP(image=IMAGE,box=BOX2)
BOX3=LOC(image=IMAGE1,object='white')
ANSWER1=COUNT(box=BOX3)
ANSWER2=EVAL(expr="'yes' if {ANSWER0} > 0 or {ANSWER1} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Are there either white cabinets or beds?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there either white cabinets or beds?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

