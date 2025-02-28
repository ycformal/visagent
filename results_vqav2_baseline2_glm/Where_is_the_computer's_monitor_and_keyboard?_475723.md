Question: Where is the computer's monitor and keyboard?

Reference Answer: on desk

Image path: ./sampled_GQA/475723.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='computer')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='monitor')
IMAGE1=CROP_ABOVE(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='keyboard')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Where is the computer's monitor and keyboard?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Where is the computer's monitor and keyboard?')=<b><span style='color: green;'>desk</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>desk</span></b></div><hr>

Answer: on the desk

