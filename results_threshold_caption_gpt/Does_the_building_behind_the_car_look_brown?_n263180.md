Question: Does the building behind the car look brown?

Reference Answer: yes

Image path: ./sampled_GQA/n263180.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='car')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='building')
ANSWER0=VQA(image=IMAGE1,question='What color is the building?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'brown' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes

