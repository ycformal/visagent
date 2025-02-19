Question: Does the person in front of the cabinets have brunette color?

Reference Answer: yes

Image path: ./sampled_GQA/n326988.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cabinets')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What color is the person?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'brunette' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FRONT'

