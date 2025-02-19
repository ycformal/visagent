Question: What is the appliance that the table is in front of?

Reference Answer: stove

Image path: ./sampled_GQA/n118102.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='table')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is in front of the table?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_FRONT'

