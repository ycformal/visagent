Question: What kind of device is the same color as the tall lamp?

Reference Answer: keyboard

Image path: ./sampled_GQA/n433692.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='lamp')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the lamp?')
BOX1=LOC(image=IMAGE,object=ANSWER0)
ANSWER1=VQA(image=IMAGE,question='What kind of device is the same color as the tall lamp?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: name 'ANSWER0' is not defined

