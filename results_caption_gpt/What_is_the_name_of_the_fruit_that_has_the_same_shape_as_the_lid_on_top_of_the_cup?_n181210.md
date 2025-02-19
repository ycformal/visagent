Question: What is the name of the fruit that has the same shape as the lid on top of the cup?

Reference Answer: orange

Image path: ./sampled_GQA/n181210.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cup')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='lid')
IMAGE1=CROP_TOP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What is the shape of the lid?')
ANSWER1=VQA(image=IMAGE,question='What is the name of the fruit that has the same shape as the lid?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: "runtime error"

