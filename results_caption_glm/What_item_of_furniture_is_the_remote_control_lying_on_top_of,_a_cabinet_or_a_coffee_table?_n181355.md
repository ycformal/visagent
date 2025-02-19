Question: What item of furniture is the remote control lying on top of, a cabinet or a coffee table?

Reference Answer: coffee table

Image path: ./sampled_GQA/n181355.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cabinet')
IMAGE0=CROP_TOPOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='remote control')
ANSWER0=COUNT(box=BOX1)
BOX2=LOC(image=IMAGE,object='coffee table')
IMAGE1=CROP_TOPOF(image=IMAGE,box=BOX2)
BOX3=LOC(image=IMAGE1,object='remote control')
ANSWER1=COUNT(box=BOX3)
ANSWER2=EVAL(expr="'cabinet' if {ANSWER0} > 0 and {ANSWER1} == 0 else 'coffee table'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Coffee table

