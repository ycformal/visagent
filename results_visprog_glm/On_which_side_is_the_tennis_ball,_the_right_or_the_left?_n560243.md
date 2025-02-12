Question: On which side is the tennis ball, the right or the left?

Reference Answer: left

Image path: ./sampled_GQA/n560243.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='tennis ball')
ANSWER0=LOCATION(box=BOX0)
ANSWER1=EVAL(expr="'right' if {ANSWER0} == 'right' else 'left'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'LOCATION'

