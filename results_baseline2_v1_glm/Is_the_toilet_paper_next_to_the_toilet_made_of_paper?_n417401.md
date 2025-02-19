Question: Is the toilet paper next to the toilet made of paper?

Reference Answer: yes

Image path: ./sampled_GQA/n417401.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='toilet paper')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='toilet')
ANSWER0=VQA(image=IMAGE0,question='What material is the toilet made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'paper' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is the toilet paper next to the toilet made of paper?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the toilet paper next to the toilet made of paper?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

