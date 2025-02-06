Question: Does the oven have the same shape as the floor?

Reference Answer: yes

Image path: ./sampled_GQA/n501609.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='oven')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='floor')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=SHAPE(image=IMAGE0)
ANSWER1=SHAPE(image=IMAGE1)
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'SHAPE'

