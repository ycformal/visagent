Question: Which person is not wearing a backpack?

Reference Answer: both

Image path: ./sampled_GQA/326928.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='backpack')
IMAGE0=CROP_WITHOUT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'no backpack' if {ANSWER0} > 0 else 'backpack'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_WITHOUT'

