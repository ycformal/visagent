Question: Does the necktie have a different color than the suit?

Reference Answer: no

Image path: ./sampled_GQA/n94074.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='necktie')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='suit')
ANSWER0=VQA(image=IMAGE0,question='What color is the necktie?')
ANSWER1=VQA(image=IMAGE1,question='What color is the suit?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0}!= {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Yes

