Question: What's in front of the wall?

Reference Answer: couch

Image path: ./sampled_GQA/n344136.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='wall')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is in front of the wall?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_FRONT'

