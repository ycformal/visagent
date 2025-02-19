Question: What material is the sturdy bridge above the river made of?

Reference Answer: concrete

Image path: ./sampled_GQA/n477215.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='river')
IMAGE0=CROP_ABOVE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='bridge')
ANSWER0=VQA(image=IMAGE1,question='What material is the sturdy bridge above the river made of?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: runtime error

