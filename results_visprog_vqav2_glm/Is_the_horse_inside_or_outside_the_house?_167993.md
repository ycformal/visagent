Question: Is the horse inside or outside the house?

Reference Answer: outside

Image path: ./sampled_GQA/167993.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='house')
IMAGE0=CROP_OUTSIDE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='horse')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'outside' if {ANSWER0} > 0 else 'inside'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_OUTSIDE'

