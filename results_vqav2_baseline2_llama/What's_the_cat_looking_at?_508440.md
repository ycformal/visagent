Question: What's the cat looking at?

Reference Answer: camera

Image path: ./sampled_GQA/508440.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='cat')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='mat')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What's the cat looking at?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What's the cat looking at?')=<b><span style='color: green;'>camera</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>camera</span></b></div><hr>

Answer: camera

