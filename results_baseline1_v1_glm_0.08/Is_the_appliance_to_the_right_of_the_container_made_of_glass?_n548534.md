Question: Is the appliance to the right of the container made of glass?

Reference Answer: yes

Image path: ./sampled_GQA/n548534.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='container')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='appliance')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
ANSWER2=VQA(image=IMAGE1,question='What material is the container made of?')
ANSWER3=EVAL(expr="'yes' if {ANSWER1} > 0 and {ANSWER2} == 'glass' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER3)
```
Answer: Runtime error: 'IMAGE1'

