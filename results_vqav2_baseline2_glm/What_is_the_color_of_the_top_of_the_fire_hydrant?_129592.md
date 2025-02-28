Question: What is the color of the top of the fire hydrant?

Reference Answer: red

Image path: ./sampled_GQA/129592.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='fire hydrant')
IMAGE0=CROP_TOP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is it?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What is the color of the top of the fire hydrant?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the color of the top of the fire hydrant?')=<b><span style='color: green;'>red</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>red</span></b></div><hr>

Answer: red

