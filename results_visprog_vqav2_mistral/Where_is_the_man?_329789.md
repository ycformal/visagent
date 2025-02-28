Question: Where is the man?

Reference Answer: dorm room

Image path: ./sampled_GQA/329789.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='man')
ANSWER0=EVAL(expr="'inside' if {BOX0} > 0 else 'outside'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: '>' not supported between instances of 'list' and 'int'

