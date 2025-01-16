Question: Is the white clock to the right or to the left of the appliance that is in front of the countertop?

Reference Answer: The clock is to the left of the freezer.

Image path: ./sampled_GQA/n140421.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='countertop')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='appliance')
IMAGE1=CROP_RIGHTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='white clock')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'right' if {ANSWER0} > 0 else 'left'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: right

