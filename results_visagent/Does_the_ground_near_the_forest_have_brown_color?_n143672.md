Question: Does the ground near the forest have brown color?

Reference Answer: No, the ground is white.

Image path: ./sampled_GQA/n143672.jpg

Program:

```
Does A <spatial pos> B have <attr>?
Program:
BOX0=LOC(image=IMAGE,object='forest')
IMAGE0=CROP_NEAR(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the ground?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'brown' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: no

