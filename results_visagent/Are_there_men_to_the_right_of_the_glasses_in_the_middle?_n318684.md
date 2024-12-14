Question: Are there men to the right of the glasses in the middle?

Reference Answer: No, the man is to the left of the glasses.

Image path: ./sampled_GQA/n318684.jpg

Program:

```
 Are A or B?
Program:
BOX0=LOC(image=IMAGE,object='glasses')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='men')
IMAGE1=CROP_RIGHTOF(image=IMAGE0,box=BOX1)
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: No

