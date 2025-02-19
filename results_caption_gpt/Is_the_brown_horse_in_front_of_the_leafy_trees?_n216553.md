Question: Is the brown horse in front of the leafy trees?

Reference Answer: no

Image path: ./sampled_GQA/n216553.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='brown horse')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='leafy trees')
IMAGE1=CROP_FRONT(image=IMAGE,box=BOX1)
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: "runtime error"

