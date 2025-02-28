Question: What number is on the man's jacket?

Reference Answer: 3

Image path: ./sampled_GQA/70134.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='man')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='jacket')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='number')
ANSWER0=VQA(image=IMAGE1,question='What number is on the jacket?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What number is on the man's jacket?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What number is on the man's jacket?')=<b><span style='color: green;'>3</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>3</span></b></div><hr>

Answer: 3

