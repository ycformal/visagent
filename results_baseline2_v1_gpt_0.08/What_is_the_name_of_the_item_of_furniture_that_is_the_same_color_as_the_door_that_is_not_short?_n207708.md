Question: What is the name of the item of furniture that is the same color as the door that is not short?

Reference Answer: bookcase

Image path: ./sampled_GQA/n207708.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='door')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the door?')
BOX1=LOC(image=IMAGE,object='furniture')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER1=VQA(image=IMAGE1,question='What color is the furniture?')
ANSWER2=EVAL(expr="'furniture' if {ANSWER0} == {ANSWER1} and not 'short' in {ANSWER1} else 'none'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What is the name of the item of furniture that is the same color as the door that is not short?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the name of the item of furniture that is the same color as the door that is not short?')=<b><span style='color: green;'>chair</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>chair</span></b></div><hr>

Answer: chair

