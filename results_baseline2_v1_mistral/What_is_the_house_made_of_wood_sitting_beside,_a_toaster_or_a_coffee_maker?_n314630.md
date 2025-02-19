Question: What is the house made of wood sitting beside, a toaster or a coffee maker?

Reference Answer: toaster

Image path: ./sampled_GQA/n314630.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='house')
IMAGE0=CROP_BESIDE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='toaster')
BOX2=LOC(image=IMAGE0,object='coffee maker')
ANSWER0=COUNT(box=BOX1)
ANSWER1=COUNT(box=BOX2)
ANSWER2=EVAL(expr="'toaster' if {ANSWER0} > 0 else 'coffee maker'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What is the house made of wood sitting beside, a toaster or a coffee maker?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the house made of wood sitting beside, a toaster or a coffee maker?')=<b><span style='color: green;'>toaster</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>toaster</span></b></div><hr>

Answer: toaster

