Question: What number is on the front of the train?

Reference Answer: 165026

Image path: ./sampled_GQA/525361.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='train')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What number is on the train?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_FRONT'

