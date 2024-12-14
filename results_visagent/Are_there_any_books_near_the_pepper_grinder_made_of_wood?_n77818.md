Question: Are there any books near the pepper grinder made of wood?

Reference Answer: Yes, there is a book near the pepper shaker.

Image path: ./sampled_GQA/n77818.jpg

Program:

```
Are there any As near B?
Program:
BOX0=LOC(image=IMAGE,object='pepper grinder')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='wood')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE,object='book')
IMAGE2=CROP_NEAR(image=IMAGE1,box=BOX2)
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes

