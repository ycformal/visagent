Question: On which side is the tennis ball, the right or the left?

Reference Answer: left

Image path: ./sampled_GQA/n560243.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='tennis ball')
ANSWER0=EVAL(expr="'right' if {BOX0} > 0 else 'left'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: '>' not supported between instances of 'list' and 'int'

