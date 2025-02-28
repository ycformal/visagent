Question: Is the person at the top or bottom of the mountain?

Reference Answer: top

Image path: ./sampled_GQA/173514.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='mountain')
IMAGE0=CROP_TOP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'top' if {ANSWER0} > 0 else 'bottom'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_TOP'

