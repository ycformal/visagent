Question: What piece of furniture is the rug in front of, a cabinet or a couch?

Reference Answer: The rug is in front of a cabinet.

Image path: ./sampled_GQA/n499081.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='rug')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='cabinet')
BOX2=LOC(image=IMAGE0,object='couch')
ANSWER0=COUNT(box=BOX1)
ANSWER1=COUNT(box=BOX2)
ANSWER2=EVAL(expr="'cabinet' if {ANSWER0} > 0 else 'couch'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'CROP_FRONT'

