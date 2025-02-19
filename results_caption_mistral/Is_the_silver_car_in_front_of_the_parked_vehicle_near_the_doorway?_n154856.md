Question: Is the silver car in front of the parked vehicle near the doorway?

Reference Answer: no

Image path: ./sampled_GQA/n154856.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='doorway')
IMAGE0=CROP_NEAR(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='parked vehicle')
IMAGE1=CROP_FRONTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='silver car')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: "runtime error"

