Question: Which is larger, the pasture or the horse?

Reference Answer: pasture

Image path: ./sampled_GQA/n324908.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='pasture')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='horse')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=SIZE(image=IMAGE0)
ANSWER1=SIZE(image=IMAGE1)
ANSWER2=EVAL(expr="'pasture' if {ANSWER0} > {ANSWER1} else 'horse'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Which is larger, the pasture or the horse?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Which is larger, the pasture or the horse?')=<b><span style='color: green;'>field</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>field</span></b></div><hr>

Answer: field

