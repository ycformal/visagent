Question: Is there a doll inside the cabinets?

Reference Answer: yes

Image path: ./sampled_GQA/n326988.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cabinets')
IMAGE0=CROP_INSIDE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='doll')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_INSIDE'

