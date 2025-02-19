Question: On which side of the image is the blue picture?

Reference Answer: right

Image path: ./sampled_GQA/n541688.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='blue picture')
ANSWER0=LOCATION(box=BOX0)
ANSWER1=EVAL(expr="'left' if {ANSWER0} == 'LEFT' else 'right'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: runtime error

