Question: What is on the top of the clock tower?

Reference Answer: flag

Image path: ./sampled_GQA/145956.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='clock tower')
IMAGE0=CROP_TOP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is on top of the clock tower?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_TOP'

