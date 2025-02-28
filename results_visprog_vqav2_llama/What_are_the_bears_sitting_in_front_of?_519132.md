Question: What are the bears sitting in front of?

Reference Answer: bed

Image path: ./sampled_GQA/519132.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bear')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='bear')
IMAGE1=CROP_BEHIND(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='bear')
IMAGE2=CROP_BEHIND(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='bear')
IMAGE3=CROP_BEHIND(image=IMAGE2,box=BOX3)
BOX4=LOC(image=IMAGE3,object='bear')
IMAGE4=CROP_BEHIND(image=IMAGE3,box=BOX4)
BOX5=LOC(image=IMAGE4,object='bear')
IMAGE5=CROP_BEHIND(image=IMAGE4,box=BOX5)
BOX6=LOC(image=IMAGE5,object='bear')
IMAGE6=CROP_BEHIND(image=IMAGE5,box=BOX6)
BOX7=LOC(image=IMAGE6,object='bear')
IMAGE7=CROP_BEHIND(image=IMAGE6,box=BOX7)
BOX8=LOC(image=IMAGE7,object='bear')
IMAGE8=CROP_BEHIND(image
```
Answer: Runtime error: ('EOF in multi-line statement', (2, 0))

