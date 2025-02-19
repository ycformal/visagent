Question: Is there any fork next to the plate?

Reference Answer: no

Image path: ./sampled_GQA/n166008.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='plate')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='fork')
IMAGE1=CROP_NEAR(image=IMAGE0,box=BOX1)
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: "runtime error"

