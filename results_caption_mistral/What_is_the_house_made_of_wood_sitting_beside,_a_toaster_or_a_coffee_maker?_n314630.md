Question: What is the house made of wood sitting beside, a toaster or a coffee maker?

Reference Answer: toaster

Image path: ./sampled_GQA/n314630.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='house')
IMAGE0=CROP_BESIDE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='toaster')
BOX2=LOC(image=IMAGE0,object='coffee maker')
ANSWER0=COUNT(box=BOX1)
ANSWER1=COUNT(box=BOX2)
ANSWER2=EVAL(expr="'toaster' if {ANSWER0} > 0 else 'coffee maker'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: runtime error

