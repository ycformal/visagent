Question: On which side of the image is the purple cabbage?

Reference Answer: right

Image path: ./sampled_GQA/n429961.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='purple cabbage')
ANSWER0=LOCATION(box=BOX0)
ANSWER1=EVAL(expr="'left' if {ANSWER0} == 'LEFT' else 'right'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'LOCATION'

