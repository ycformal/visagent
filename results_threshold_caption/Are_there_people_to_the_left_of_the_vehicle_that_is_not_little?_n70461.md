Question: Are there people to the left of the vehicle that is not little?

Reference Answer: No, the people are to the right of the train.

Image path: ./sampled_GQA/n70461.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='vehicle')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and not 'little' in {IMAGE0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes

