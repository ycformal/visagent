Question: Is the umbrella in the bottom part of the picture?

Reference Answer: no

Image path: ./sampled_GQA/n403734.jpg

Program:

```
BOX0=GET(image=IMAGE)
IMAGE0=CROP_BOTTOMOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='umbrella')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_BOTTOMOF'

