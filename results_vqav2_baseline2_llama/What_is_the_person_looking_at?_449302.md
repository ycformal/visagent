Question: What is the person looking at?

Reference Answer: water

Image path: ./sampled_GQA/449302.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='looking at')
ANSWER0=VQA(image=IMAGE0,question='What is the person looking at?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What is the person looking at?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the person looking at?')=<b><span style='color: green;'>water</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>water</span></b></div><hr>

Answer: water

