Question: How big is the donut the person holds?

Reference Answer: small

Image path: ./sampled_GQA/n318370.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='donut')
ANSWER0=SIZE(box=BOX1)
ANSWER1=EVAL(expr="'small' if {ANSWER0} < 0.5 else 'big'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'SIZE'

