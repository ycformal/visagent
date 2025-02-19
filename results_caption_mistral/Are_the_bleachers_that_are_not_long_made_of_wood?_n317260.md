Question: Are the bleachers that are not long made of wood?

Reference Answer: no

Image path: ./sampled_GQA/n317260.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bleachers')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='long')
IMAGE1=CROP_NOT(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='wood')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: "runtime error"

