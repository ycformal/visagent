Question: Who is standing against the surfboard?

Reference Answer: woman

Image path: ./sampled_GQA/n298104.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='surfboard')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'person' if {ANSWER0} > 0 else'surfboard'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Who is standing against the surfboard?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Who is standing against the surfboard?')=<b><span style='color: green;'>woman</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>woman</span></b></div><hr>

Answer: woman

