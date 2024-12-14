Question: Is the food in the paper container topped with chicken?

Reference Answer: Yes, the hot dog is topped with chicken.

Image path: ./sampled_GQA/2413987.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='paper container')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='food')
IMAGE1=CROP_TOPPEDWITH(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='chicken')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_TOPPEDWITH'

