Question: Is the long fence behind or in front of the tree made of wood?

Reference Answer: behind

Image path: ./sampled_GQA/n260521.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='tree')
IMAGE0=CROP_BEHIND(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='long fence')
ANSWER0=VQA(image=IMAGE1,question='What material is the long fence made of?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'IMAGE1'

