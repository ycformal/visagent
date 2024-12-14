Question: Is he in front of the net above the floor?

Reference Answer: No, the man is behind the net.

Image path: ./sampled_GQA/n282607.jpg

Program:

```
 Is A <spatial pos> B?
Program:
BOX0=LOC(image=IMAGE,object='net')
IMAGE0=CROP_ABOVE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='floor')
IMAGE1=CROP_FRONT(image=IMAGE0,box=BOX1)
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes

