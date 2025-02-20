Question: What do you think is parked in front of the fire truck that is shown in the photograph?

Reference Answer: car

Image path: ./sampled_GQA/n480253.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='fire truck')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What do you think is parked in front of the fire truck?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What do you think is parked in front of the fire truck that is shown in the photograph?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What do you think is parked in front of the fire truck that is shown in the photograph?')=<b><span style='color: green;'>car</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>car</span></b></div><hr>

Answer: car

