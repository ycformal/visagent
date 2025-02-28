Question: How many people are facing away from the players?

Reference Answer: 3

Image path: ./sampled_GQA/559842.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='players')
IMAGE0=CROP_AWAYFROM(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='people')
ANSWER0=COUNT(box=BOX1)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_AWAYFROM'

