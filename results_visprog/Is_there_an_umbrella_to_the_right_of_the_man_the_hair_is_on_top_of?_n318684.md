Question: Is there an umbrella to the right of the man the hair is on top of?

Reference Answer: Yes, there is an umbrella to the right of the man.

Image path: ./sampled_GQA/n318684.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='man')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='hair')
IMAGE1=CROP_TOP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='umbrella')
IMAGE2=CROP_RIGHTOF(image=IMAGE1,box=BOX2)
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_TOP'

