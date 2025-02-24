Question: How is the item of furniture that is made of same material as the floor called?

Reference Answer: bookcase

Image path: ./sampled_GQA/n69237.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='floor')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the floor made of?')
BOX1=LOC(image=IMAGE,object=ANSWER0)
ANSWER1=VQA(image=IMAGE,question='How is the item of furniture that is made of {ANSWER0} called?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: name 'ANSWER0' is not defined

