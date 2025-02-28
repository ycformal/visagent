Question: What is the color of the closest building?

Reference Answer: yellow

Image path: ./sampled_GQA/552507.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='building')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='building')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='building')
IMAGE2=CROP(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='building')
IMAGE3=CROP(image=IMAGE2,box=BOX3)
BOX4=LOC(image=IMAGE3,object='building')
IMAGE4=CROP(image=IMAGE3,box=BOX4)
BOX5=LOC(image=IMAGE4,object='building')
IMAGE5=CROP(image=IMAGE4,box=BOX5)
BOX6=LOC(image=IMAGE5,object='building')
IMAGE6=CROP(image=IMAGE5,box=BOX6)
BOX7=LOC(image=IMAGE6,object='building')
IMAGE7=CROP(image=IMAGE6,box=BOX7)
BOX8=LOC(image=IMAGE7,object='building')
IMAGE8=CROP(image=IMAGE7,box=BOX8)
BOX9=LOC(image=IMAGE8,object='building')
IMAGE9
```
Answer: Runtime error: ''

