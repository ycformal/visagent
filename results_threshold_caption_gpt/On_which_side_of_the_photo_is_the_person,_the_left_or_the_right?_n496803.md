Question: On which side of the photo is the person, the left or the right?

Reference Answer: right

Image path: ./sampled_GQA/n496803.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='person')
ANSWER0=EVAL(expr="'left' if {BOX0.x} < IMAGE.width/2 else 'right'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: right

