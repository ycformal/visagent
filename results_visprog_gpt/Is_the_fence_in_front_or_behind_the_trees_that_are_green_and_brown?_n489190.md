Question: Is the fence in front or behind the trees that are green and brown?

Reference Answer: behind

Image path: ./sampled_GQA/n489190.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='trees')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='green')
BOX2=LOC(image=IMAGE0,object='brown')
IMAGE1=CROP_FRONT(image=IMAGE0,box1=BOX1,box2=BOX2)
BOX3=LOC(image=IMAGE1,object='fence')
ANSWER0=COUNT(box=BOX3)
ANSWER1=EVAL(expr="'front' if {ANSWER0} > 0 else 'behind'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FRONT'

