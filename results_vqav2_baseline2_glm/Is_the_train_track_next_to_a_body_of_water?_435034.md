Question: Is the train track next to a body of water?

Reference Answer: no

Image path: ./sampled_GQA/435034.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='train track')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='water')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is the train track next to a body of water?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the train track next to a body of water?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

