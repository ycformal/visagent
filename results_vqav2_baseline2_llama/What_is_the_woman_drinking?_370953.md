Question: What is the woman drinking?

Reference Answer: water

Image path: ./sampled_GQA/370953.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='woman')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='drink')
ANSWER0=VQA(image=IMAGE0,question='What is the woman drinking?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What is the woman drinking?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the woman drinking?')=<b><span style='color: green;'>water</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>water</span></b></div><hr>

Answer: water

