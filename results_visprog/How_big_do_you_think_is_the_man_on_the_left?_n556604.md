Question: How big do you think is the man on the left?

Reference Answer: The man is large.

Image path: ./sampled_GQA/n556604.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='LEFT')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='man')
ANSWER0=SIZE(box=BOX1)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'SIZE'

