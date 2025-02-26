Question: Do you see instruments next to the fireplace?

Reference Answer: yes

Image path: ./sampled_GQA/n302387.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='fireplace')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='instruments')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Do you see instruments next to the fireplace?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Do you see instruments next to the fireplace?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

