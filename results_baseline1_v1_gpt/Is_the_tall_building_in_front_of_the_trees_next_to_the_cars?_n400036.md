Question: Is the tall building in front of the trees next to the cars?

Reference Answer: no

Image path: ./sampled_GQA/n400036.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='trees')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='tall building')
IMAGE1=CROP_FRONT(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='cars')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FRONT'

