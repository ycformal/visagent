Question: Is there any speaker in the picture that is not white?

Reference Answer: no

Image path: ./sampled_GQA/n315887.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='speakers')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='white')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} < {COUNT(box=BOX0)} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'COUNT(box=BOX0)'

