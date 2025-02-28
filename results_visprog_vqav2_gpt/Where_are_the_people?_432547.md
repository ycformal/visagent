Question: Where are the people?

Reference Answer: school

Image path: ./sampled_GQA/432547.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='people')
ANSWER0=EVAL(expr="'top' if {BOX0}.y < IMAGE.height/2 else 'bottom'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'list' object has no attribute 'y'

