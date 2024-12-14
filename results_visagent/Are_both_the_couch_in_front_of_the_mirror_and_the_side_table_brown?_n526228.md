Question: Are both the couch in front of the mirror and the side table brown?

Reference Answer: Yes, both the couch and the side table are brown.

Image path: ./sampled_GQA/n526228.jpg

Program:

```
 Are A and B both <attr>?
Program:
BOX0=LOC(image=IMAGE,object='couch')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='mirror')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE,object='side table')
IMAGE2=CROP(image=IMAGE,box=BOX2)
ANSWER0=VQA(image=IMAGE0,question='What color is the couch?')
ANSWER1=VQA(image=IMAGE1,question='What color is the mirror?')
ANSWER2=VQA(image=IMAGE2,question='What color is the side table?')
ANSWER3=EVAL(expr="'yes' if {ANSWER0} == 'brown' and {ANSWER1} == 'brown' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER3)
```
Answer: Yes

