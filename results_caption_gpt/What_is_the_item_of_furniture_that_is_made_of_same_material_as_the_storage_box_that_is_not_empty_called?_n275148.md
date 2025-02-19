Question: What is the item of furniture that is made of same material as the storage box that is not empty called?

Reference Answer: desk

Image path: ./sampled_GQA/n275148.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='storage box')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the storage box made of?')
BOX1=LOC(image=IMAGE,object='furniture')
IMAGE1=CROP_SAME_MATERIAL(image=IMAGE,box=BOX1,material=ANSWER0)
ANSWER1=VQA(image=IMAGE1,question='What is the item of furniture?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: runtime error

