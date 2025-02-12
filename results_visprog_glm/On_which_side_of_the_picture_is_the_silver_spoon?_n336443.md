Question: On which side of the picture is the silver spoon?

Reference Answer: right

Image path: ./sampled_GQA/n336443.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='silver spoon')
ANSWER0=LOCATION(box=BOX0)
ANSWER1=EVAL(expr="'left' if {ANSWER0} == 'LEFT' else 'right'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'LOCATION'

