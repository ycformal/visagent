Question: Is the bench in front of the woman the man is to the left of?

Reference Answer: Yes, the bench is in front of the woman.

Image path: ./sampled_GQA/n451187.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='woman')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='bench')
IMAGE1=CROP_FRONT(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE,object='man')
IMAGE2=CROP_LEFTOF(image=IMAGE,box=BOX2)
ANSWER0=COUNT(box=BOX1)
ANSWER1=COUNT(box=BOX2)
ANSWER2=EVAL(expr="'yes' if {ANSWER0} > 0 and {ANSWER1} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: no

