Question: Are there cookies that are not baked?

Reference Answer: no

Image path: ./sampled_GQA/n470131.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cookies')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='baked')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} < {ANSWER2} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'ANSWER2'

