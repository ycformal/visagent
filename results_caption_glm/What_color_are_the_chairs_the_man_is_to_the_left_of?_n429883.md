Question: What color are the chairs the man is to the left of?

Reference Answer: white

Image path: ./sampled_GQA/n429883.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='LEFT')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='man')
IMAGE1=CROP_LEFTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='chairs')
ANSWER0=VQA(image=IMAGE2,question='What color are the chairs?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: "runtime error"

