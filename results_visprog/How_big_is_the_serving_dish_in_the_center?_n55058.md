Question: How big is the serving dish in the center?

Reference Answer: The serving dish is small.

Image path: ./sampled_GQA/n55058.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='center')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='serving dish')
ANSWER0=SIZE(box=BOX1)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'SIZE'

