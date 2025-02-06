Question: What appliance is on top of the oven?

Reference Answer: stove

Image path: ./sampled_GQA/n398429.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='oven')
IMAGE0=CROP_TOPOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='appliance')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_TOPOF'

