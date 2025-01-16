Question: Is the person that is not fat holding a camera?

Reference Answer: No, the man is holding the glass.

Image path: ./sampled_GQA/n52544.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='fat')
IMAGE1=CROP_NOT(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='camera')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes

