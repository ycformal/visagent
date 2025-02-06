Question: Are the tall buildings behind the sand that is not dirty?

Reference Answer: yes

Image path: ./sampled_GQA/n90944.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='sand')
IMAGE0=CROP_NOT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='dirty')
IMAGE1=CROP_BEHIND(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='tall buildings')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_NOT'

