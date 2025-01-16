Question: Does the vehicle on the field seem to be small?

Reference Answer: Yes, the vehicle is small.

Image path: ./sampled_GQA/n497789.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='field')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='vehicle')
ANSWER0=SIZE(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} < 50 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: yes

