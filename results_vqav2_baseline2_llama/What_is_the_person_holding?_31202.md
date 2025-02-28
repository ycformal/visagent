Question: What is the person holding?

Reference Answer: skis

Image path: ./sampled_GQA/31202.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
IMAGE1=CROP_BELOW(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='person')
IMAGE2=CROP_BELOW(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='person')
IMAGE3=CROP_BELOW(image=IMAGE2,box=BOX3)
BOX4=LOC(image=IMAGE3,object='person')
IMAGE4=CROP_BELOW(image=IMAGE3,box=BOX4)
BOX5=LOC(image=IMAGE4,object='person')
IMAGE5=CROP_BELOW(image=IMAGE4,box=BOX5)
BOX6=LOC(image=IMAGE5,object='person')
IMAGE6=CROP_BELOW(image=IMAGE5,box=BOX6)
BOX7=LOC(image=IMAGE6,object='person')
IMAGE7=CROP_BELOW(image=IMAGE6,box=BOX7)
BOX8=LOC(image=IMAGE7,object='person')
IMAGE8=CROP_BELOW(image=IMAGE7,box=
```
Answer: skis

