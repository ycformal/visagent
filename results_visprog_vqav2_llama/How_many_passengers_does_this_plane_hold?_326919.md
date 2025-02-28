Question: How many passengers does this plane hold?

Reference Answer: 100

Image path: ./sampled_GQA/326919.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='plane')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='passengers')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'{ANSWER0}' passengers")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: unexpected EOF while parsing (<string>, line 1)

