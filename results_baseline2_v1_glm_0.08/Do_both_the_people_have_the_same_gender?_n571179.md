Question: Do both the people have the same gender?

Reference Answer: no

Image path: ./sampled_GQA/n571179.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='people')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='male')
ANSWER0=COUNT(box=BOX1)
BOX2=LOC(image=IMAGE0,object='female')
ANSWER1=COUNT(box=BOX2)
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Do both the people have the same gender?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Do both the people have the same gender?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

