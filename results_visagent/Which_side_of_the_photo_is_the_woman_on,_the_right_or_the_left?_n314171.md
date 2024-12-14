Question: Which side of the photo is the woman on, the right or the left?

Reference Answer: The woman is on the right of the image.

Image path: ./sampled_GQA/n314171.jpg

Program:

```
Which side is A?
Program:
BOX0=LOC(image=IMAGE,object='woman')
ANSWER0=EVAL(expr="'right' if {BOX0.x} > IMAGE.width/2 else 'left'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: right

