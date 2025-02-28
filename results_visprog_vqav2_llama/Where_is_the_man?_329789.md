Question: Where is the man?

Reference Answer: dorm room

Image path: ./sampled_GQA/329789.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='man')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='TOP')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='RIGHT')
IMAGE2=CROP(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='LEFT')
IMAGE3=CROP(image=IMAGE2,box=BOX3)
BOX4=LOC(image=IMAGE3,object='BOTTOM')
IMAGE4=CROP(image=IMAGE3,box=BOX4)
ANSWER0=COUNT(box=BOX1)
ANSWER1=COUNT(box=BOX2)
ANSWER2=COUNT(box=BOX3)
ANSWER3=COUNT(box=BOX4)
ANSWER4=EVAL(expr="'top' if {ANSWER0} > 0 else 'bottom'")
ANSWER5=EVAL(expr="'right' if {ANSWER1} > 0 else 'left'")
ANSWER6=EVAL(expr="'top' if {ANSWER2} > 0 else 'bottom'")
ANSWER7=EVAL(expr="'right' if {ANSWER3} >
```
Answer: Runtime error: ('EOF in multi-line statement', (2, 0))

