Question: Which is larger, the pasture or the horse?

Reference Answer: The pasture is larger than the horse.

Image path: ./sampled_GQA/n324908.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='pasture')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='horse')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=AREA(image=IMAGE0)
ANSWER1=AREA(image=IMAGE1)
ANSWER2=EVAL(expr="'pasture' if {ANSWER0} > {ANSWER1} else 'horse'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'AREA'

