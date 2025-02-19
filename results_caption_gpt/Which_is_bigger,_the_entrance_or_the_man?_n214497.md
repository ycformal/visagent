Question: Which is bigger, the entrance or the man?

Reference Answer: entrance

Image path: ./sampled_GQA/n214497.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='entrance')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='man')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=SIZE(image=IMAGE0)
ANSWER1=SIZE(image=IMAGE1)
ANSWER2=EVAL(expr="'entrance' if {ANSWER0} > {ANSWER1} else 'man'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: "runtime error"

