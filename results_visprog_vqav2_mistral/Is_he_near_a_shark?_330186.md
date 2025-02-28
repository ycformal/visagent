Question: Is he near a shark?

Reference Answer: no

Image path: ./sampled_GQA/330186.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='shark')
IMAGE0=CROP_NEAR(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_NEAR'

