Question: Are both the palm tree in front of the wall and the palm to the left of the flag brown?

Reference Answer: yes

Image path: ./sampled_GQA/n507959.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='palm tree')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='wall')
IMAGE1=CROP_FRONT(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE,object='palm')
IMAGE2=CROP_LEFTOF(image=IMAGE,box=BOX2)
BOX3=LOC(image=IMAGE2,object='flag')
IMAGE3=CROP_LEFTOF(image=IMAGE2,box=BOX3)
ANSWER0=VQA(image=IMAGE1,question='What color is the palm tree?')
ANSWER1=VQA(image=IMAGE3,question='What color is the palm?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'brown' and {ANSWER1} == 'brown' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Are both the palm tree in front of the wall and the palm to the left of the flag brown?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are both the palm tree in front of the wall and the palm to the left of the flag brown?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

