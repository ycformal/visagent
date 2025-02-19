Question: Are there people to the left of the vehicle that is not little?

Reference Answer: no

Image path: ./sampled_GQA/n70461.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='vehicle')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='LEFT')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='person')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: runtime error

