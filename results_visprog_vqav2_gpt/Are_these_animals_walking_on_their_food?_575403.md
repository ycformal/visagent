Question: Are these animals walking on their food?

Reference Answer: yes

Image path: ./sampled_GQA/575403.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='food')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='animals')
IMAGE1=CROP_ON(image=IMAGE0,box=BOX1)
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_ON'

