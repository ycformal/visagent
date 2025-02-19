Question: Are both the urinal that is white and silver and the urinal that is white and silver made of porcelain?

Reference Answer: yes

Image path: ./sampled_GQA/n503626.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='urinal',attributes=['white','silver'])
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the urinal made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'porcelain' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Are both the urinal that is white and silver and the urinal that is white and silver made of porcelain?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are both the urinal that is white and silver and the urinal that is white and silver made of porcelain?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

