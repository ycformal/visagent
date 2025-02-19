Question: Are there any traffic signs or trucks that are large?

Reference Answer: yes

Image path: ./sampled_GQA/n155555.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='traffic sign')
BOX1=LOC(image=IMAGE,object='truck')
ANSWER0=COUNT(box=BOX0)
ANSWER1=COUNT(box=BOX1)
ANSWER2=EVAL(expr="'yes' if {ANSWER0} + {ANSWER1} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Are there any traffic signs or trucks that are large?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there any traffic signs or trucks that are large?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes.

