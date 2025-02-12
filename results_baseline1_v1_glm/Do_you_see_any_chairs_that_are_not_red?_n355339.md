Question: Do you see any chairs that are not red?

Reference Answer: no

Image path: ./sampled_GQA/n355339.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='chairs')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='chairs',color='red')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} < {COUNT} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'COUNT'

