Question: What is the name on the front of the train?

Reference Answer: trimet

Image path: ./sampled_GQA/534639.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='train')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the name on the front of the train?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_FRONT'

