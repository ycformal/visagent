Question: Is the bread on the left side?

Reference Answer: no

Image path: ./sampled_GQA/n278312.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bread')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and {LEFT} == 'left' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'LEFT'

