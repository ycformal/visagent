Question: Is there a traffic light in front of the bridge that is crossing the street?

Reference Answer: no

Image path: ./sampled_GQA/n309148.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bridge')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='traffic light')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: "runtime error"

