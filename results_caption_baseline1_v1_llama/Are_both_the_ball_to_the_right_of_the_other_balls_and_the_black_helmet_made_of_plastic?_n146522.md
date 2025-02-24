Question: Are both the ball to the right of the other balls and the black helmet made of plastic?

Reference Answer: yes

Image path: ./sampled_GQA/n146522.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='ball')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='ball')
IMAGE1=CROP_RIGHTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='ball')
IMAGE2=CROP_RIGHTOF(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='ball')
IMAGE3=CROP_RIGHTOF(image=IMAGE2,box=BOX3)
BOX4=LOC(image=IMAGE3,object='ball')
IMAGE4=CROP_RIGHTOF(image=IMAGE3,box=BOX4)
BOX5=LOC(image=IMAGE4,object='ball')
IMAGE5=CROP_RIGHTOF(image=IMAGE4,box=BOX5)
BOX6=LOC(image=IMAGE5,object='ball')
IMAGE6=CROP_RIGHTOF(image=IMAGE5,box=BOX6)
BOX7=LOC(image=IMAGE6,object='ball')
IMAGE7=CROP_RIGHTOF(image=IMAGE6,box=BOX7)
BOX8=LOC(image=IMAGE7,object='ball')
IMAGE8=CROP_RIGHTOF(image=IMAGE7,box=
```
Answer: Runtime error: ('EOF in multi-line statement', (2, 0))

