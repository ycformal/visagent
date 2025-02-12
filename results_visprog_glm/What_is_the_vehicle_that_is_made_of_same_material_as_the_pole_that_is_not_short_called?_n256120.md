Question: What is the vehicle that is made of same material as the pole that is not short called?

Reference Answer: van

Image path: ./sampled_GQA/n256120.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='pole')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='short')
IMAGE1=CROP_NOT(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='vehicle')
ANSWER0=VQA(image=IMAGE,question='What is the vehicle that is made of same material as the pole that is not short called?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_NOT'

