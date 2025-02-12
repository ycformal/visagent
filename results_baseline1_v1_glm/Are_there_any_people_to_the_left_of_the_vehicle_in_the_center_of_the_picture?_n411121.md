Question: Are there any people to the left of the vehicle in the center of the picture?

Reference Answer: no

Image path: ./sampled_GQA/n411121.jpg

Program:

```
BOX0=GET(image=IMAGE)
IMAGE0=CROP_CENTER(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='vehicle')
IMAGE1=CROP_LEFTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='people')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_CENTER'

