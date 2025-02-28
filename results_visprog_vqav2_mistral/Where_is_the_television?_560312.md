Question: Where is the television?

Reference Answer: on wall

Image path: ./sampled_GQA/560312.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='television')
ANSWER0=EVAL(expr="'left' if {BOX0}.x < 0.5 else 'right'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'list' object has no attribute 'x'

