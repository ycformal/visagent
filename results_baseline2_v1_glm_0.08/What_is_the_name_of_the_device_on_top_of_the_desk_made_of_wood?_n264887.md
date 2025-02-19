Question: What is the name of the device on top of the desk made of wood?

Reference Answer: monitor

Image path: ./sampled_GQA/n264887.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='desk')
IMAGE0=CROP_TOPOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='device')
ANSWER0=VQA(image=IMAGE0,question='What is the name of the device?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What is the name of the device on top of the desk made of wood?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the name of the device on top of the desk made of wood?')=<b><span style='color: green;'>computer</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>computer</span></b></div><hr>

Answer: computer

