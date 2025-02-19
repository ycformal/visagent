Question: Do you see any toilets near the clean sink?

Reference Answer: yes

Image path: ./sampled_GQA/n153293.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='sink')
IMAGE0=CROP_NEAR(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='toilet')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_NEAR'

