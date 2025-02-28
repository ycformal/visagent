Question: Why is this cat climbing?

Reference Answer: window

Image path: ./sampled_GQA/372979.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='cat')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='mat')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Why is this cat climbing?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Why is this cat climbing?')=<b><span style='color: green;'>window</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>window</span></b></div><hr>

Answer: window

