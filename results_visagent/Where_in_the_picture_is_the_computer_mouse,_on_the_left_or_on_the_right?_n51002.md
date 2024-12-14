Question: Where in the picture is the computer mouse, on the left or on the right?

Reference Answer: The computer mouse is on the right of the image.

Image path: ./sampled_GQA/n51002.jpg

Program:

```
Where is A in the picture?
Program:
BOX0=LOC(image=IMAGE,object='computer mouse')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Where in the picture is the computer mouse?')
ANSWER1=EVAL(expr="'left' if {ANSWER0} < 0.5 else 'right'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: right

