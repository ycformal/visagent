Question: What is the item of furniture that is made of same material as the table the silverware is on called?

Reference Answer: shelf

Image path: ./sampled_GQA/n460385.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='table')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='silverware')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='furniture')
IMAGE2=CROP(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='material')
IMAGE3=CROP(image=IMAGE2,box=BOX3)
BOX4=LOC(image=IMAGE3,object='table')
IMAGE4=CROP(image=IMAGE3,box=BOX4)
BOX5=LOC(image=IMAGE4,object='silverware')
IMAGE5=CROP(image=IMAGE4,box=BOX5)
BOX6=LOC(image=IMAGE5,object='furniture')
IMAGE6=CROP(image=IMAGE5,box=BOX6)
BOX7=LOC(image=IMAGE6,object='material')
IMAGE7=CROP(image=IMAGE6,box=BOX7)
ANSWER0=VQA(image=IMAGE7,question='What is the item of furniture that is made of same material as the table the silverware is on called?')
FINAL_RESULT
```
Answer: Runtime error: ''

