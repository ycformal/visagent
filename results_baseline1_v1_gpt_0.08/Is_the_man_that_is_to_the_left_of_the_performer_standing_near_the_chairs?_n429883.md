Question: Is the man that is to the left of the performer standing near the chairs?

Reference Answer: yes

Image path: ./sampled_GQA/n429883.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='performer')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='man')
IMAGE1=CROP_NEAR(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='chairs')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_NEAR'

