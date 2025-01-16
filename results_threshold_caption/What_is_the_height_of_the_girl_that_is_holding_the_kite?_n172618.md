Question: What is the height of the girl that is holding the kite?

Reference Answer: The girl is tall.

Image path: ./sampled_GQA/n172618.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='girl')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='kite')
IMAGE1=CROP_BELOW(image=IMAGE0,box=BOX1)
ANSWER0=HEIGHT(box=BOX0)
ANSWER1=HEIGHT(box=BOX1)
ANSWER2=EVAL(expr="{ANSWER0} - {ANSWER1}")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: 3 feet

