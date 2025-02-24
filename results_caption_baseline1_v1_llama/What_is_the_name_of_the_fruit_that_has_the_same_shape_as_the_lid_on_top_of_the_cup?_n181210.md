Question: What is the name of the fruit that has the same shape as the lid on top of the cup?

Reference Answer: orange

Image path: ./sampled_GQA/n181210.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cup')
IMAGE0=CROP_TOP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='lid')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='fruit')
IMAGE2=CROP(image=IMAGE,box=BOX2)
ANSWER0=VQA(image=IMAGE2,question='What is the name of the fruit?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_TOP'

