Question: Are the bleachers that are not long made of wood?

Reference Answer: no

Image path: ./sampled_GQA/n317260.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bleachers')
IMAGE0=CROP_NOTLONG(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material are the bleachers made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'wood' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_NOTLONG'

