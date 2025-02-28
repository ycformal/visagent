Question: Does the curtain cover the entire window?

Reference Answer: yes

Image path: ./sampled_GQA/428041.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='window')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='curtain')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Does the curtain cover the entire window?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the curtain cover the entire window?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

