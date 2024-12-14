Question: Are there screens to the right of the monitor that is not off?

Reference Answer: No, the screen is to the left of the monitor.

Image path: ./sampled_GQA/n513429.jpg

Program:

```
 Are A <planar pos> B and B <attr>?
Program:
BOX0=LOC(image=IMAGE,object='monitor')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='screen')
IMAGE1=CROP_RIGHTOF(image=IMAGE0,box=BOX1)
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and {IMAGE0} != 'off' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes

