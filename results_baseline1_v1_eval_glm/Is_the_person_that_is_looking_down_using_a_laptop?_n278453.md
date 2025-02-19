Question: Is the person that is looking down using a laptop?

Reference Answer: no

Image path: ./sampled_GQA/n278453.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='laptop')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

