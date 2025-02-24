Question: What type of vehicle is she in front of, a bus or a car?

Reference Answer: car

Image path: ./sampled_GQA/n24526.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='bus')
BOX2=LOC(image=IMAGE0,object='car')
ANSWER0=COUNT(box=BOX1)
ANSWER1=COUNT(box=BOX2)
ANSWER2=EVAL(expr="'bus' if {ANSWER0} > 0 else 'car'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'CROP_FRONT'

