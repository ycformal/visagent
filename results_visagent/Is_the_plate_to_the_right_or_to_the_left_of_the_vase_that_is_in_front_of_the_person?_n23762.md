Question: Is the plate to the right or to the left of the vase that is in front of the person?

Reference Answer: The plate is to the right of the vase.

Image path: ./sampled_GQA/n23762.jpg

Program:

```
 Is A <planar pos> or <planar pos> B?
Program:
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='vase')
IMAGE1=CROP_FRONT(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='plate')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'right' if {ANSWER0} > 0 else 'left'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: right

