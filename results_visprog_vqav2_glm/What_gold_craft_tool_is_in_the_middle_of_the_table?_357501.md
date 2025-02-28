Question: What gold craft tool is in the middle of the table?

Reference Answer: scissors

Image path: ./sampled_GQA/357501.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='table')
IMAGE0=CROP_CENTER(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='craft tool')
ANSWER0=VQA(image=IMAGE0,question='What gold craft tool is in the middle of the table?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_CENTER'

