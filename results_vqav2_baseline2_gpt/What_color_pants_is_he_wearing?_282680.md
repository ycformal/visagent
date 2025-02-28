Question: What color pants is he wearing?

Reference Answer: black

Image path: ./sampled_GQA/282680.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color pants is he wearing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What color pants is he wearing?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color pants is he wearing?')=<b><span style='color: green;'>black</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>black</span></b></div><hr>

Answer: black

