Question: What is the person that is not short doing?

Reference Answer: looking down

Image path: ./sampled_GQA/n566028.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='short')
IMAGE0=CROP_NOT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=VQA(image=IMAGE1,question='What is the person that is not short doing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: runtime error

