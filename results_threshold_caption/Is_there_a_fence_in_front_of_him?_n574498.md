Question: Is there a fence in front of him?

Reference Answer: No, the fence is behind the man.

Image path: ./sampled_GQA/n574498.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='him')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='fence')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes
