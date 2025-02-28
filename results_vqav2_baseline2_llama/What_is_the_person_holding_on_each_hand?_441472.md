Question: What is the person holding on each hand?

Reference Answer: gloves

Image path: ./sampled_GQA/441472.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='hand')
IMAGE1=CROP_RIGHTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='person')
IMAGE2=CROP(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='hand')
IMAGE3=CROP_RIGHTOF(image=IMAGE2,box=BOX3)
BOX4=LOC(image=IMAGE3,object='person')
IMAGE4=CROP(image=IMAGE3,box=BOX4)
BOX5=LOC(image=IMAGE4,object='hand')
IMAGE5=CROP_RIGHTOF(image=IMAGE4,box=BOX5)
BOX6=LOC(image=IMAGE5,object='person')
IMAGE6=CROP(image=IMAGE5,box=BOX6)
BOX7=LOC(image=IMAGE6,object='hand')
IMAGE7=CROP_RIGHTOF(image=IMAGE6,box=BOX7)
BOX8=LOC(image=IMAGE7,object='person')
IMAGE8=CROP(image=IMAGE7,box=BOX8)
BOX9=LOC(image=IMAGE
```
Answer: gloves

