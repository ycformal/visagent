Question: Is the brown horse in front of the leafy trees?

Reference Answer: no

Image path: ./sampled_GQA/n216553.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='horse')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='trees')
IMAGE1=CROP_FRONT(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='brown')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FRONT'

