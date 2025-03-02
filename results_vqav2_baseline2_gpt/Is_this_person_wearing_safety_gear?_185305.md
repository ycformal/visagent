Question: Is this person wearing safety gear?

Reference Answer: no

Image path: ./sampled_GQA/185305.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the person wearing?')
ANSWER1=EVAL(expr="'yes' if 'safety gear' in {ANSWER0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is this person wearing safety gear?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is this person wearing safety gear?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

