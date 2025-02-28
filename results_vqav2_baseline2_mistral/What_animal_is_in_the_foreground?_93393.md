Question: What animal is in the foreground?

Reference Answer: giraffe

Image path: ./sampled_GQA/93393.jpg

Original program:

```
BOX0=GET(image=IMAGE)
IMAGE0=CROP_FOREGROUND(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='animal')
ANSWER0=VQA(image=IMAGE0,question='What animal is in the foreground?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What animal is in the foreground?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What animal is in the foreground?')=<b><span style='color: green;'>giraffe</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>giraffe</span></b></div><hr>

Answer: giraffe

