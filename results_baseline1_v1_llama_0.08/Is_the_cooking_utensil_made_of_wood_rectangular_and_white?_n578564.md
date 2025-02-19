Question: Is the cooking utensil made of wood rectangular and white?

Reference Answer: no

Image path: ./sampled_GQA/n578564.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cooking utensil')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='wood')
BOX2=LOC(image=IMAGE0,object='rectangle')
BOX3=LOC(image=IMAGE0,object='white')
ANSWER0=COUNT(box=BOX1)
ANSWER1=COUNT(box=BOX2)
ANSWER2=COUNT(box=BOX3)
ANSWER3=EVAL(expr="'yes' if {ANSWER0} > 0 and {ANSWER1} > 0 and {ANSWER2} > 0 and {ANSWER3} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER3)
```
Answer: Runtime error: 'ANSWER3'

