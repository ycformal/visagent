Question: What is beside the sidewalk?

Reference Answer: bus

Image path: ./sampled_GQA/38540.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='sidewalk')
IMAGE0=CROP_BESIDE(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is beside the sidewalk?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_BESIDE'

