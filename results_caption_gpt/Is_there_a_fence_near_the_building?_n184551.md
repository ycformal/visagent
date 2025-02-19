Question: Is there a fence near the building?

Reference Answer: no

Image path: ./sampled_GQA/n184551.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='building')
IMAGE0=CROP_NEAR(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='fence')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: "runtime error"

