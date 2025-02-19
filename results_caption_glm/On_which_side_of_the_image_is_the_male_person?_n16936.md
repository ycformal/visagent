Question: On which side of the image is the male person?

Reference Answer: left

Image path: ./sampled_GQA/n16936.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='male')
ANSWER0=LOCATION(box=BOX0)
ANSWER1=EVAL(expr="'left' if {ANSWER0} == 'LEFT' else 'right'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: "runtime error"

