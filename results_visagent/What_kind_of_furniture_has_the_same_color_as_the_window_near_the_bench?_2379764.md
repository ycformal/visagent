Question: What kind of furniture has the same color as the window near the bench?

Reference Answer: The bed is the same color as the window.

Image path: ./sampled_GQA/2379764.jpg

Program:

```
 What kind of A has the same <attr> as B <spatial pos> C?
Program:
BOX0=LOC(image=IMAGE,object='window')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='bench')
IMAGE1=CROP_NEAR(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='What color is the window?')
ANSWER1=VQA(image=IMAGE1,question='What kind of furniture is near the bench?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: table

