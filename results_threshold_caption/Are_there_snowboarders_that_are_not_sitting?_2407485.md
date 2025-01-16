Question: Are there snowboarders that are not sitting?

Reference Answer: No, there is a snowboarder but he is sitting.

Image path: ./sampled_GQA/2407485.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='snowboarder')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='sitting')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} < {BOX0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: yes

