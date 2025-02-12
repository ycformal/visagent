Question: Is the umbrella in the bottom part of the picture?

Reference Answer: no

Image path: ./sampled_GQA/n403734.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='umbrella')
IMAGE0=CROP_BOTTOM(image=IMAGE,box=BOX0)
ANSWER0=COUNT(box=IMAGE0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_BOTTOM'

