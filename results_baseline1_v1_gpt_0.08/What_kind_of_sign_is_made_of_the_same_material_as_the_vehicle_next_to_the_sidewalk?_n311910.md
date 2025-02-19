Question: What kind of sign is made of the same material as the vehicle next to the sidewalk?

Reference Answer: street sign

Image path: ./sampled_GQA/n311910.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='vehicle')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='sidewalk')
IMAGE1=CROP_RIGHTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='sign')
ANSWER0=VQA(image=IMAGE0,question='What material is the vehicle made of?')
ANSWER1=VQA(image=IMAGE1,question='What material is the sidewalk made of?')
ANSWER2=VQA(image=IMAGE2,question='What kind of sign is made of {ANSWER0} material?')
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'IMAGE2'

