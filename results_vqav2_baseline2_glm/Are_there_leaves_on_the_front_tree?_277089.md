Question: Are there leaves on the front tree?

Reference Answer: no

Image path: ./sampled_GQA/277089.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='tree')
IMAGE0=CROP_FRONTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='leaves')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Are there leaves on the front tree?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there leaves on the front tree?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

