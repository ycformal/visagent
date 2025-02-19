Question: Does the soccer player next to the other soccer player look small?

Reference Answer: yes

Image path: ./sampled_GQA/n244826.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='soccer player')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='soccer player')
IMAGE1=CROP_RIGHTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='soccer player')
IMAGE2=CROP_RIGHTOF(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='soccer player')
IMAGE3=CROP_RIGHTOF(image=IMAGE2,box=BOX3)
BOX4=LOC(image=IMAGE3,object='soccer player')
IMAGE4=CROP_RIGHTOF(image=IMAGE3,box=BOX4)
BOX5=LOC(image=IMAGE4,object='soccer player')
IMAGE5=CROP_RIGHTOF(image=IMAGE4,box=BOX5)
BOX6=LOC(image=IMAGE5,object='soccer player')
IMAGE6=CROP_RIGHTOF(image=IMAGE5,box=BOX6)
BOX7=LOC(image=IMAGE6,object='soccer player')
IMAGE7=CROP_RIGHTOF(image=IMAGE6,box=BOX7)
BOX8=LOC(image=IMAGE7,object
```
Answer: Runtime error: ('EOF in multi-line statement', (2, 0))

