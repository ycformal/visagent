Question: Is the toilet paper that is to the right of the chair resting on a lamp?

Reference Answer: no

Image path: ./sampled_GQA/n59147.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='chair')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='toilet paper')
IMAGE1=CROP_ON(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='lamp')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_ON'

