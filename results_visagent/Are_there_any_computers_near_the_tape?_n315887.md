Question: Are there any computers near the tape?

Reference Answer: Yes, there is a computer near the tape.

Image path: ./sampled_GQA/n315887.jpg

Program:

```
 Are A near B?
Program:
BOX0=LOC(image=IMAGE,object='tape')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='computer')
IMAGE1=CROP_NEAR(image=IMAGE,box=BOX1)
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes

