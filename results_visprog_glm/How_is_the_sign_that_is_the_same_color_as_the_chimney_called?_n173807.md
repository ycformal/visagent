Question: How is the sign that is the same color as the chimney called?

Reference Answer: street sign

Image path: ./sampled_GQA/n173807.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='chimney')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the chimney?')
BOX1=LOC(image=IMAGE,object=ANSWER0)
ANSWER1=VQA(image=IMAGE,question='How is the sign that is the same color as the chimney called?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: name 'ANSWER0' is not defined

