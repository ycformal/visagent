Question: What is the vehicle that is made of same material as the pole that is not short called?

Reference Answer: van

Image path: ./sampled_GQA/n256120.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='pole')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the pole made of?')
BOX1=LOC(image=IMAGE,object='vehicle')
IMAGE1=CROP_DIFFERENTMATERIAL(image=IMAGE,box=BOX1,material=ANSWER0)
ANSWER1=VQA(image=IMAGE1,question='What is the vehicle called?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_DIFFERENTMATERIAL'

