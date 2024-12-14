Question: Do you see towels to the left of the shower curtain that is in front of the bathtub?

Reference Answer: No, there is a girl to the left of the shower curtain.

Image path: ./sampled_GQA/n473688.jpg

Program:

```
 Do A <planar pos> B <spatial pos> C?
Program:
BOX0=LOC(image=IMAGE,object='bathtub')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='shower curtain')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='towels')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: No

