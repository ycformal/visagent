Question: On which side is the coach?

Reference Answer: left

Image path: ./sampled_GQA/n317260.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='coach')
ANSWER0=LOCATION(box=BOX0)
ANSWER1=EVAL(expr="'left' if {ANSWER0} == 'LEFT' else 'right'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: runtime error

