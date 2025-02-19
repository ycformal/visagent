Question: Is the white vehicle on the right or on the left side of the image?

Reference Answer: right

Image path: ./sampled_GQA/n124651.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='white vehicle')
ANSWER0=EVAL(expr="'right' if {BOX0[0]} > IMAGE.width/2 else 'left'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: name 'IMAGE' is not defined

