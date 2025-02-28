Question: What is on top of the train?

Reference Answer: nothing

Image path: ./sampled_GQA/252968.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='train')
IMAGE0=CROP_TOP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is on top of the train?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_TOP'

