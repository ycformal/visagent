Question: Is there any short grass in the picture?

Reference Answer: yes

Image path: ./sampled_GQA/n98540.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='grass')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='short')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is there any short grass in the picture?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there any short grass in the picture?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

