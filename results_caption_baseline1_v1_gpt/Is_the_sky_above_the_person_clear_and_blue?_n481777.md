Question: Is the sky above the person clear and blue?

Reference Answer: no

Image path: ./sampled_GQA/n481777.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='sky')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes.

