Question: What animal is next to the giraffe?

Reference Answer: antelope

Image path: ./sampled_GQA/479203.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='giraffe')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What animal is next to the giraffe?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_NEXTTO'

