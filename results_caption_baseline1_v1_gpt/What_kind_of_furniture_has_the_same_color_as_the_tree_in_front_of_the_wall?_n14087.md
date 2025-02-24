Question: What kind of furniture has the same color as the tree in front of the wall?

Reference Answer: couch

Image path: ./sampled_GQA/n14087.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='tree')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='wall')
IMAGE1=CROP_BEHIND(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What color is the tree?')
ANSWER1=VQA(image=IMAGE1,question='What kind of furniture has the same color as the tree?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FRONT'

