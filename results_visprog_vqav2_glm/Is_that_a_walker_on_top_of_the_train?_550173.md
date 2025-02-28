Question: Is that a walker on top of the train?

Reference Answer: no

Image path: ./sampled_GQA/550173.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='train')
IMAGE0=CROP_TOP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='walker')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_TOP'

