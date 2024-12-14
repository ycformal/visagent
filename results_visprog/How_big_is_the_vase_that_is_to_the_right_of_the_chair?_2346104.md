Question: How big is the vase that is to the right of the chair?

Reference Answer: The vase is large.

Image path: ./sampled_GQA/2346104.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='chair')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='vase')
ANSWER0=SIZE(box=BOX1)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'SIZE'

