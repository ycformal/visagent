Question: Is the train track next to a body of water?

Reference Answer: no

Image path: ./sampled_GQA/435034.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='train track')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='water')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_NEXTTO'

