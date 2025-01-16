Question: Is there any woman in this photo that is not riding?

Reference Answer: Yes, there is a woman that is skateboarding.

Image path: ./sampled_GQA/2381410.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='woman')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='riding')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} < {BOX0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: No

