Question: Is the mirror in front of the woman made of glass?

Reference Answer: yes

Image path: ./sampled_GQA/n455563.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='woman')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='mirror')
IMAGE1=CROP_FRONT(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What material is the mirror made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'glass' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: "runtime error"

