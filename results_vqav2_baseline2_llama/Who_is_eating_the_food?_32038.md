Question: Who is eating the food?

Reference Answer: people

Image path: ./sampled_GQA/32038.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='food')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Who is eating the food?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Who is eating the food?')=<b><span style='color: green;'>no one</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no one</span></b></div><hr>

Answer: no one

