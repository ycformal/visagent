Question: Does the chair in front of the table look brown or white?

Reference Answer: brown

Image path: ./sampled_GQA/n4777.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='table')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='chair')
IMAGE1=CROP_FRONT(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What color is the chair?')
ANSWER1=EVAL(expr="'brown' if {ANSWER0} == 'brown' else 'white'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: "runtime error"

