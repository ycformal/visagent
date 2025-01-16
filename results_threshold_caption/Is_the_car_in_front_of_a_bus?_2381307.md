Question: Is the car in front of a bus?

Reference Answer: No, the car is in front of the jeep.

Image path: ./sampled_GQA/2381307.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bus')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='car')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: no

