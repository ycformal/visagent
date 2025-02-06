Question: What is the name of the item of furniture that is the same color as the door that is not short?

Reference Answer: bookcase

Image path: ./sampled_GQA/n207708.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='door')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='short')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='furniture')
IMAGE2=CROP(image=IMAGE,box=BOX2)
BOX3=LOC(image=IMAGE2,object='door')
IMAGE3=CROP(image=IMAGE,box=BOX3)
BOX4=LOC(image=IMAGE3,object='furniture')
IMAGE4=CROP(image=IMAGE,box=BOX4)
BOX5=LOC(image=IMAGE4,object='furniture')
IMAGE5=CROP(image=IMAGE,box=BOX5)
BOX6=LOC(image=IMAGE5,object='door')
IMAGE6=CROP(image=IMAGE,box=BOX6)
BOX7=LOC(image=IMAGE6,object='furniture')
IMAGE7=CROP(image=IMAGE,box=BOX7)
BOX8=LOC(image=IMAGE7,object='furniture')
IMAGE8=CROP(image=IMAGE,box=BOX8)
BOX9=LOC(image=IMAGE8,object='door')
IMAGE9=CROP(image
```
Answer: Runtime error: ('EOF in multi-line statement', (2, 0))

