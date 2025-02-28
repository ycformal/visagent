Question: Where is the man?

Reference Answer: dorm room

Image path: ./sampled_GQA/329789.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='man')
ANSWER0=EVAL(expr="'top' if {BOX0}.y < IMAGE.height/2 else 'bottom'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'list' object has no attribute 'y'

