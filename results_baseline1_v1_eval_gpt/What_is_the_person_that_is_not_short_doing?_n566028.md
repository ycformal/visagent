Question: What is the person that is not short doing?

Reference Answer: looking down

Image path: ./sampled_GQA/n566028.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP_NOTSHORT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the person doing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_NOTSHORT'

