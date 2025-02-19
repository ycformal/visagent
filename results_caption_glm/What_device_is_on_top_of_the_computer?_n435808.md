Question: What device is on top of the computer?

Reference Answer: router

Image path: ./sampled_GQA/n435808.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='computer')
IMAGE0=CROP_TOPOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='device')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: runtime error

