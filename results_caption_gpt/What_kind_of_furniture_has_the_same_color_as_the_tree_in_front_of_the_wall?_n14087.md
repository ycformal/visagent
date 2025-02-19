Question: What kind of furniture has the same color as the tree in front of the wall?

Reference Answer: couch

Image path: ./sampled_GQA/n14087.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='tree')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the tree?')
BOX1=LOC(image=IMAGE,object='wall')
IMAGE1=CROP_FRONT(image=IMAGE,box=BOX1)
ANSWER1=VQA(image=IMAGE1,question='What color is the wall?')
ANSWER2=EVAL(expr="'furniture' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: runtime error

