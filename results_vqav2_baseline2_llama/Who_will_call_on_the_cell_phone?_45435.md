Question: Who will call on the cell phone?

Reference Answer: anyone

Image path: ./sampled_GQA/45435.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='cell phone')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'the person on the left' if {ANSWER0} > 0 else 'the person on the right'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Who will call on the cell phone?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Who will call on the cell phone?')=<b><span style='color: green;'>woman</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>woman</span></b></div><hr>

Answer: woman

