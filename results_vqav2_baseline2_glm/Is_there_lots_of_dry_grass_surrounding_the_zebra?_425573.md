Question: Is there lots of dry grass surrounding the zebra?

Reference Answer: yes

Image path: ./sampled_GQA/425573.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='zebra')
IMAGE0=CROP_AROUND(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='grass')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is there lots of dry grass surrounding the zebra?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there lots of dry grass surrounding the zebra?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

