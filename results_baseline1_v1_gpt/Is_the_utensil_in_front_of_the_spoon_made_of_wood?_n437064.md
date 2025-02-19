Question: Is the utensil in front of the spoon made of wood?

Reference Answer: no

Image path: ./sampled_GQA/n437064.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='spoon')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='utensil')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FRONT'

