Question: Are there people to the left of the vehicle that is not little?

Reference Answer: no

Image path: ./sampled_GQA/n70461.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='vehicle')
BOX1=LOC(image=IMAGE,object='little')
BOX2=SUBTRACT(box=BOX0,box=BOX1)
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX2)
BOX3=LOC(image=IMAGE0,object='people')
ANSWER0=COUNT(box=BOX3)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes.

