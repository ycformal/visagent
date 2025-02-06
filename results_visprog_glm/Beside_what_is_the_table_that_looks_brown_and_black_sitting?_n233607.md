Question: Beside what is the table that looks brown and black sitting?

Reference Answer: shelf

Image path: ./sampled_GQA/n233607.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='table')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='brown')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='black')
IMAGE2=CROP(image=IMAGE0,box=BOX2)
BOX3=LOC(image=IMAGE2,object='sitting')
ANSWER0=VQA(image=IMAGE3,question='Beside what is the table that looks brown and black sitting?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'IMAGE3'

