Question: Are the kids on the right?

Reference Answer: Yes, the kids are on the right of the image.

Image path: ./sampled_GQA/2333428.jpg

Program:

```
 Are A on the <planar pos>?
Program:
BOX0=LOC(image=IMAGE,object='kids')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
ANSWER0=COUNT(box=BOX0)
ANSWER1=COUNT(box=BOX1)
ANSWER2=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Yes.

