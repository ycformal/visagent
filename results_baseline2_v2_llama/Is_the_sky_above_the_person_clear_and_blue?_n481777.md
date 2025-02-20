Question: Is the sky above the person clear and blue?

Reference Answer: no

Image path: ./sampled_GQA/n481777.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='sky')
IMAGE1=CROP_ABOVE(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What color is the sky?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'clear blue' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='sky')
IMAGE1=CROP_ABOVE(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What color is the sky?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'clear blue' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes

