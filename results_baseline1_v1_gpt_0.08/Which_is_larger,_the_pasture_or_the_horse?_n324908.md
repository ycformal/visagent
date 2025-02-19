Question: Which is larger, the pasture or the horse?

Reference Answer: pasture

Image path: ./sampled_GQA/n324908.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='pasture')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='horse')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=SIZE(image=IMAGE0)
ANSWER1=SIZE(image=IMAGE1)
ANSWER2=EVAL(expr="'pasture' if {ANSWER0} > {ANSWER1} else 'horse'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'SIZE'

