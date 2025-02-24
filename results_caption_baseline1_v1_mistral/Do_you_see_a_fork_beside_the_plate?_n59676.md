Question: Do you see a fork beside the plate?

Reference Answer: no

Image path: ./sampled_GQA/n59676.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='plate')
IMAGE0=CROP_BESIDE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='fork')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes.

