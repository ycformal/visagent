Question: What does the back of the vehicle say?

Reference Answer: sturgis or bust

Image path: ./sampled_GQA/422870.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='vehicle')
IMAGE0=CROP_BACK(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What does the back of the vehicle say?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_BACK'

