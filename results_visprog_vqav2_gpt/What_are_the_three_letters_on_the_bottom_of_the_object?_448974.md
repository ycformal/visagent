Question: What are the three letters on the bottom of the object?

Reference Answer: lg

Image path: ./sampled_GQA/448974.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='BOTTOM')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=OCR(image=IMAGE0,box=BOX0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'OCR'

