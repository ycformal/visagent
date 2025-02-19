Question: What bag is made of the same material as the trash can beside the wall?

Reference Answer: trash bag

Image path: ./sampled_GQA/n530733.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='wall')
IMAGE0=CROP_BESIDE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='trash can')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What material is the trash can made of?')
ANSWER1=VQA(image=IMAGE,question='What bag is made of {ANSWER0}?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_BESIDE'

