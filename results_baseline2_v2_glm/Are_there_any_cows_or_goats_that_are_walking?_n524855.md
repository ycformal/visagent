Question: Are there any cows or goats that are walking?

Reference Answer: no

Image path: ./sampled_GQA/n524855.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='cows')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='goats')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='walking')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Are there any cows or goats that are walking?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there any cows or goats that are walking?')=<b><span style='color: green;'>cows</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>cows</span></b></div><hr>

Answer: cows

