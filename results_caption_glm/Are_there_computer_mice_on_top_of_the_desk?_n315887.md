Question: Are there computer mice on top of the desk?

Reference Answer: yes

Image path: ./sampled_GQA/n315887.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='desk')
IMAGE0=CROP_TOPOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='computer mouse')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: No.

