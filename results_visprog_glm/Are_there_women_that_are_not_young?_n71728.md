Question: Are there women that are not young?

Reference Answer: yes

Image path: ./sampled_GQA/n71728.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='women')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='young')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} < {TOTAL} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'TOTAL'

