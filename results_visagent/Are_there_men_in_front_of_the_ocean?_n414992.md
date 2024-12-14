Question: Are there men in front of the ocean?

Reference Answer: Yes, there is a man in front of the ocean.

Image path: ./sampled_GQA/n414992.jpg

Program:

```
 Are A <spatial pos> B?
Program:
BOX0=LOC(image=IMAGE,object='ocean')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='men')
IMAGE1=CROP_FRONT(image=IMAGE,box=BOX1)
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes

