Question: Are there any women to the left of the man the light fixture is facing?

Reference Answer: no

Image path: ./sampled_GQA/n429883.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='light fixture')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Which direction is the light fixture facing?')
ANSWER1=EVAL(expr="'right' if {ANSWER0} == 'left' else 'left'")
BOX1=GET(image=IMAGE)
IMAGE1=CROP(image=IMAGE,box=BOX1)
IMAGE2=CROP(image=IMAGE1,side={ANSWER1})
BOX2=LOC(image=IMAGE2,object='man')
IMAGE3=CROP(image=IMAGE2,box=BOX2)
IMAGE4=CROP(image=IMAGE3,side={ANSWER1})
BOX3=LOC(image=IMAGE4,object='woman')
ANSWER2=COUNT(box=BOX3)
ANSWER3=EVAL(expr="'yes' if {ANSWER2} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER3)
```
Answer: Runtime error: 'box'

