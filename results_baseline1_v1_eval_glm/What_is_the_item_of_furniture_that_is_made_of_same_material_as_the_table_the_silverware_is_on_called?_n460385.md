Question: What is the item of furniture that is made of same material as the table the silverware is on called?

Reference Answer: shelf

Image path: ./sampled_GQA/n460385.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='table')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='silverware')
IMAGE1=CROP_BELOW(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='furniture')
ANSWER0=VQA(image=IMAGE2,question='What is the item of furniture that is made of same material as the table the silverware is on called?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'IMAGE2'

