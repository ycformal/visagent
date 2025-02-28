Question: What is the man sitting on top of?

Reference Answer: chair

Image path: ./sampled_GQA/125208.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='man')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='chair')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What is the man sitting on top of?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the man sitting on top of?')=<b><span style='color: green;'>couch</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>couch</span></b></div><hr>

Answer: couch

