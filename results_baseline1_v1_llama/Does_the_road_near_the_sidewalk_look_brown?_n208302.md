Question: Does the road near the sidewalk look brown?

Reference Answer: no

Image path: ./sampled_GQA/n208302.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='sidewalk')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='road')
IMAGE1=CROP_RIGHTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='road')
IMAGE2=CROP_RIGHTOF(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='road')
IMAGE3=CROP_RIGHTOF(image=IMAGE2,box=BOX3)
BOX4=LOC(image=IMAGE3,object='road')
IMAGE4=CROP_RIGHTOF(image=IMAGE3,box=BOX4)
BOX5=LOC(image=IMAGE4,object='road')
IMAGE5=CROP_RIGHTOF(image=IMAGE4,box=BOX5)
BOX6=LOC(image=IMAGE5,object='road')
IMAGE6=CROP_RIGHTOF(image=IMAGE5,box=BOX6)
BOX7=LOC(image=IMAGE6,object='road')
IMAGE7=CROP_RIGHTOF(image=IMAGE6,box=BOX7)
BOX8=LOC(image=IMAGE7,object='road')
IMAGE8=CROP_RIGHTOF(image=IMAGE7,
```
Answer: Runtime error: tile cannot extend outside image

