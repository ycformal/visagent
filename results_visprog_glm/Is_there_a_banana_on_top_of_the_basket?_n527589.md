Question: Is there a banana on top of the basket?

Reference Answer: yes

Image path: ./sampled_GQA/n527589.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='basket')
IMAGE0=CROP_TOP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='banana')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_TOP'

