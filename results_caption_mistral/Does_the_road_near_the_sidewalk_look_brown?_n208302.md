Question: Does the road near the sidewalk look brown?

Reference Answer: no

Image path: ./sampled_GQA/n208302.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='sidewalk')
IMAGE0=CROP_NEAR(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='road')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='Does the road look brown?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: "runtime error"

