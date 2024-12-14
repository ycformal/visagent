Question: Is the utensil in front of the spoon made of wood?

Reference Answer: No, the utensil is made of metal.

Image path: ./sampled_GQA/n437064.jpg

Program:

```
 Is A <spatial pos> B made of <material>?
Program:
BOX0=LOC(image=IMAGE,object='spoon')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='utensil')
IMAGE1=CROP_FRONT(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What material is the utensil made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'wood' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: No

