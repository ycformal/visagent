Question: What kind of furniture has the same color as the tree in front of the wall?

Reference Answer: couch

Image path: ./sampled_GQA/n14087.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='tree')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='wall')
IMAGE1=CROP_FRONT(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What color is the wall?')
ANSWER1=VQA(image=IMAGE,question='What kind of furniture has the same color as the wall?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: christmas tree

