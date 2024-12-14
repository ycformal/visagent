Question: Is the silver knife under the pizza on the plate?

Reference Answer: Yes, the knife is under the pizza.

Image path: ./sampled_GQA/2350614.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='plate')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='pizza')
IMAGE1=CROP_ONTOP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='silver knife')
IMAGE2=CROP_BELOW(image=IMAGE1,box=BOX2)
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_ONTOP'

