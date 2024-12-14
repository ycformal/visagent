Question: How big are the waffles on top of the plate?

Reference Answer: The waffles are small.

Image path: ./sampled_GQA/n100991.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='plate')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='waffles')
ANSWER0=SIZE(box=BOX1)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'SIZE'

