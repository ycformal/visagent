Question: Are there any gloves or hats that are not large?

Reference Answer: No, there is a hat but it is large.

Image path: ./sampled_GQA/n460556.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='gloves')
BOX1=LOC(image=IMAGE,object='hats')
ANSWER0=COUNT(box=BOX0)
ANSWER1=COUNT(box=BOX1)
ANSWER2=EVAL(expr="'yes' if {ANSWER0} + {ANSWER1} > 0 and else 'no'")
BOX2=LOC(image=IMAGE,object='large')
ANSWER3=COUNT(box=BOX2)
ANSWER4=EVAL(expr="'yes' if {ANSWER3} == 0 else 'no'")
ANSWER5=EVAL(expr="'yes' if {ANSWER2} == 'yes' and {ANSWER4} == 'yes' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER5)
```
Answer: Yes

