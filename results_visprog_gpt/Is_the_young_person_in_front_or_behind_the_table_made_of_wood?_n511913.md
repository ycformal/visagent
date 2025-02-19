Question: Is the young person in front or behind the table made of wood?

Reference Answer: front

Image path: ./sampled_GQA/n511913.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='table')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='wood')
IMAGE1=CROP_FRONT(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='young person')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'front' if {ANSWER0} > 0 else 'behind'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FRONT'

