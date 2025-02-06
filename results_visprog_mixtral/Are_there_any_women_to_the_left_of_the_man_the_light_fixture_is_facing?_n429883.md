Question: Are there any women to the left of the man the light fixture is facing?

Reference Answer: no

Image path: ./sampled_GQA/n429883.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='light fixture')
IMAGE0=CROP_FACING(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='man')
IMAGE1=CROP_LEFTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='woman')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FACING'

