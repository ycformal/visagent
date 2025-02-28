Question: What is the woman standing in front of?

Reference Answer: tv

Image path: ./sampled_GQA/351489.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='woman')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the woman standing in front of?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_FRONT'

