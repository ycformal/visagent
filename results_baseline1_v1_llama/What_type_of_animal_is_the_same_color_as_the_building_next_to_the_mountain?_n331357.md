Question: What type of animal is the same color as the building next to the mountain?

Reference Answer: calf

Image path: ./sampled_GQA/n331357.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='mountain')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='building')
IMAGE1=CROP_RIGHTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='animal')
IMAGE2=CROP_RIGHTOF(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='animal')
IMAGE3=CROP_RIGHTOF(image=IMAGE2,box=BOX3)
BOX4=LOC(image=IMAGE3,object='animal')
IMAGE4=CROP_RIGHTOF(image=IMAGE3,box=BOX4)
BOX5=LOC(image=IMAGE4,object='animal')
IMAGE5=CROP_RIGHTOF(image=IMAGE4,box=BOX5)
BOX6=LOC(image=IMAGE5,object='animal')
IMAGE6=CROP_RIGHTOF(image=IMAGE5,box=BOX6)
BOX7=LOC(image=IMAGE6,object='animal')
IMAGE7=CROP_RIGHTOF(image=IMAGE6,box=BOX7)
BOX8=LOC(image=IMAGE7,object='animal')
IMAGE8=CROP_RIGHTOF(image=IMAGE7,box
```
Answer: Runtime error: ('EOF in multi-line statement', (2, 0))

