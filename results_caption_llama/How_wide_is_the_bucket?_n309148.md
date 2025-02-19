Question: How wide is the bucket?

Reference Answer: wide

Image path: ./sampled_GQA/n309148.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bucket')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='bucket')
ANSWER0=WIDTH(box=BOX1)
ANSWER1=EVAL(expr="'wide' if {ANSWER0} > 100 else 'narrow'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: runtime error

