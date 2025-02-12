Question: Are the electrical outlets and the drawers made of the same material?

Reference Answer: no

Image path: ./sampled_GQA/n35676.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='electrical outlet')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='drawers')
ANSWER0=VQA(image=IMAGE0,question='What material is the electrical outlet made of?')
ANSWER1=VQA(image=IMAGE1,question='What material is the drawers made of?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'IMAGE1'

