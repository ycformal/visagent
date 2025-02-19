Question: Is the skateboarder that is not female wearing a hat?

Reference Answer: no

Image path: ./sampled_GQA/n16936.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='skateboarder')
IMAGE0=CROP_NOT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='female')
IMAGE1=CROP_NOT(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='hat')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_NOT'

