Question: Is the person in front of the frame healthy and adult?

Reference Answer: no

Image path: ./sampled_GQA/n234683.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='frame')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FRONT'

