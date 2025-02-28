Question: What is the woman in red pointing at?

Reference Answer: field

Image path: ./sampled_GQA/185240.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='woman')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='red')
IMAGE1=CROP_WHATSOVER(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What is the woman in red pointing at?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_WHATSOVER'

