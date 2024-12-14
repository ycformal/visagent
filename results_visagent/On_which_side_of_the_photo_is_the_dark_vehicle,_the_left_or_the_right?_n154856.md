Question: On which side of the photo is the dark vehicle, the left or the right?

Reference Answer: The van is on the left of the image.

Image path: ./sampled_GQA/n154856.jpg

Program:

```
 On which side of the photo is A, the left or the right?
Program:
BOX0=LOC(image=IMAGE,object='dark vehicle')
ANSWER0=EVAL(expr="'left' if {BOX0[0]} < IMAGE.width/2 else 'right'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: left

