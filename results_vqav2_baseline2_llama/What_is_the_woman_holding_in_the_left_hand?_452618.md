Question: What is the woman holding in the left hand?

Reference Answer: glass

Image path: ./sampled_GQA/452618.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='woman')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='hand')
IMAGE1=CROP_BELOW(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='object')
ANSWER0=VQA(image=IMAGE1,question='What is the object?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What is the woman holding in the left hand?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the woman holding in the left hand?')=<b><span style='color: green;'>glass</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>glass</span></b></div><hr>

Answer: glass

