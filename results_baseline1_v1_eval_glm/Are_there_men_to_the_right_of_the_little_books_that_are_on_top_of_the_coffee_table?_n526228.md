Question: Are there men to the right of the little books that are on top of the coffee table?

Reference Answer: no

Image path: ./sampled_GQA/n526228.jpg

Program:

```
BOX0=EVAL(expr="[[0,0,{IMAGE.size[0]}-1,{IMAGE.size[1]}-1]]")
IMAGE0=CROP_ABOVE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='coffee table')
IMAGE1=CROP_TOPRIGHTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='little books')
IMAGE2=CROP_RIGHTOF(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='men')
ANSWER0=COUNT(box=BOX3)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_TOPRIGHTOF'

