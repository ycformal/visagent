Question: What item of furniture is on top of the sidewalk?

Reference Answer: table

Image path: ./sampled_GQA/n501951.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='sidewalk')
IMAGE0=CROP_TOPOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='furniture')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_TOPOF'

