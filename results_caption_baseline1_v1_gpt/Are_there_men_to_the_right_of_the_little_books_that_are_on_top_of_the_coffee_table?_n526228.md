Question: Are there men to the right of the little books that are on top of the coffee table?

Reference Answer: no

Image path: ./sampled_GQA/n526228.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='coffee table')
IMAGE0=CROP_ABOVE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='little books')
IMAGE1=CROP_ONTOP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='men')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_ONTOP'

