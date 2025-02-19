Question: Does the thin man face a lamp?

Reference Answer: no

Image path: ./sampled_GQA/n52544.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='thin man')
IMAGE0=CROP_FACING(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='lamp')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FACING'

