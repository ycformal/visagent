Question: How large are the sailboats underneath the boats?

Reference Answer: The sailboats are small.

Image path: ./sampled_GQA/n386688.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='boats')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='sailboats')
ANSWER0=SIZE(box=BOX1)
ANSWER1=EVAL(expr="'small' if {ANSWER0} < 100 else 'medium' if {ANSWER0} < 500 else 'large'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'SIZE'

