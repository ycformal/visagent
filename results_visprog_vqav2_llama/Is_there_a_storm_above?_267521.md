Question: Is there a storm above?

Reference Answer: no

Image path: ./sampled_GQA/267521.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='storm')
IMAGE0=CROP_ABOVE(image=IMAGE,box=BOX0)
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'BOX1'

