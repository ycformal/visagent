Question: What is the girl in front of?

Reference Answer: trees

Image path: ./sampled_GQA/n137182.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='girl')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='TOP')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='TOP')
IMAGE2=CROP(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='TOP')
IMAGE3=CROP(image=IMAGE2,box=BOX3)
BOX4=LOC(image=IMAGE3,object='TOP')
IMAGE4=CROP(image=IMAGE3,box=BOX4)
BOX5=LOC(image=IMAGE4,object='TOP')
IMAGE5=CROP(image=IMAGE4,box=BOX5)
BOX6=LOC(image=IMAGE5,object='TOP')
IMAGE6=CROP(image=IMAGE5,box=BOX6)
BOX7=LOC(image=IMAGE6,object='TOP')
IMAGE7=CROP(image=IMAGE6,box=BOX7)
BOX8=LOC(image=IMAGE7,object='TOP')
IMAGE8=CROP(image=IMAGE7,box=BOX8)
BOX9=LOC(image=IMAGE8,object='TOP')
IMAGE9
```
Answer: Runtime error: ''

