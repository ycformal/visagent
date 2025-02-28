Question: What letters on front of the train?

Reference Answer: mata

Image path: ./sampled_GQA/205206.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='train')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What letters are on the front of the train?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_FRONT'

