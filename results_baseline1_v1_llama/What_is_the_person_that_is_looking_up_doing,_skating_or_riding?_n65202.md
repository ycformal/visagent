Question: What is the person that is looking up doing, skating or riding?

Reference Answer: skating

Image path: ./sampled_GQA/n65202.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='skateboard')
IMAGE1=CROP_BELOW(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='person')
IMAGE2=CROP_BELOW(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='skateboard')
IMAGE3=CROP_BELOW(image=IMAGE2,box=BOX3)
BOX4=LOC(image=IMAGE3,object='person')
IMAGE4=CROP_BELOW(image=IMAGE3,box=BOX4)
BOX5=LOC(image=IMAGE4,object='skateboard')
IMAGE5=CROP_BELOW(image=IMAGE4,box=BOX5)
BOX6=LOC(image=IMAGE5,object='person')
IMAGE6=CROP_BELOW(image=IMAGE5,box=BOX6)
BOX7=LOC(image=IMAGE6,object='skateboard')
IMAGE7=CROP_BELOW(image=IMAGE6,box=BOX7)
BOX8=LOC(image=IMAGE7,object='person')
IMAGE8=CROP_BE
```
Answer: Runtime error: 'CROP_BE'

