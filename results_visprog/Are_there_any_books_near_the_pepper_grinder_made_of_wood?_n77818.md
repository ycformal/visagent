Question: Are there any books near the pepper grinder made of wood?

Reference Answer: Yes, there is a book near the pepper shaker.

Image path: ./sampled_GQA/n77818.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='pepper grinder')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='wood')
IMAGE1=CROP_NEAR(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='books')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_NEAR'

