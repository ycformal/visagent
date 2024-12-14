Question: Are there women that are not sitting?

Reference Answer: Yes, there is a woman that is pointing.

Image path: ./sampled_GQA/2406736.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='woman')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='sitting')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} < {BOX0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: '<' not supported between instances of 'int' and 'list'

