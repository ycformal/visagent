Question: Does the road near the sidewalk look brown?

Reference Answer: no

Image path: ./sampled_GQA/n208302.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='sidewalk')
IMAGE0=CROP_NEAR(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='road')
ANSWER0=VQA(image=IMAGE0,question='What color is the road?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'brown' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: no

