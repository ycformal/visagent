Question: Does the chair in front of the table look brown or white?

Reference Answer: brown

Image path: ./sampled_GQA/n4777.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='table')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='chair')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'brown' if {ANSWER0} > 0 else 'white'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FRONT'

