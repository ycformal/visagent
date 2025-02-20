Question: What's in front of the wall?

Reference Answer: couch

Image path: ./sampled_GQA/n344136.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='wall')
IMAGE0=CROP_BEHIND(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='car')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'car' if {ANSWER0} > 0 else 'nothing'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What's in front of the wall?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What's in front of the wall?')=<b><span style='color: green;'>couch</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>couch</span></b></div><hr>

Answer: couch

