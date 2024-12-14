Question: How big is the animal in the middle of the image?

Reference Answer: The cat is small.

Image path: ./sampled_GQA/n433692.jpg

Program:

```
How <attr> is A in the middle of the image?
Program:
BOX0=LOC(image=IMAGE,object='all')
IMAGE0=CROP_CENTER(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='animal')
ANSWER0=VQA(image=IMAGE0,question='How big is the animal?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: medium

