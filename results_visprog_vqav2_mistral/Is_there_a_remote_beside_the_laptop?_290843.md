Question: Is there a remote beside the laptop?

Reference Answer: no

Image path: ./sampled_GQA/290843.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='laptop')
IMAGE0=CROP_BESIDE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='remote')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_BESIDE'

