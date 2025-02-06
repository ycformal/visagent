Question: Which side of the image is the brown house on?

Reference Answer: right

Image path: ./sampled_GQA/n357126.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='brown house')
ANSWER0=LOCATION(box=BOX0)
ANSWER1=EVAL(expr="'left' if {ANSWER0} == 'LEFT' else 'right'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'LOCATION'

