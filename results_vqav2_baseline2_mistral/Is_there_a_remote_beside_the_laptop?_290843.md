Question: Is there a remote beside the laptop?

Reference Answer: no

Image path: ./sampled_GQA/290843.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='laptop')
IMAGE0=CROP_BESIDE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='remote')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is there a remote beside the laptop?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a remote beside the laptop?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

