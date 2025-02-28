Question: What color is the man's shirt?

Reference Answer: yellow

Image path: ./sampled_GQA/501439.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='man')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the man's shirt?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What color is the man's shirt?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the man's shirt?')=<b><span style='color: green;'>yellow</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yellow</span></b></div><hr>

Answer: yellow

