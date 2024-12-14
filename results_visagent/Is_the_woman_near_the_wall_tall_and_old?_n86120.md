Question: Is the woman near the wall tall and old?

Reference Answer: No, the woman is old but short.

Image path: ./sampled_GQA/n86120.jpg

Program:

```
 Is A <spatial pos> B and <attr>?
Program:
BOX0=LOC(image=IMAGE,object='wall')
IMAGE0=CROP_NEAR(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='woman')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
ANSWER2=VQA(image=IMAGE0,question='What is the height of the woman?')
ANSWER3=VQA(image=IMAGE0,question='What is the age of the woman?')
ANSWER4=EVAL(expr="'yes' if {ANSWER1} and {ANSWER2} == 'tall' and {ANSWER3} == 'old' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER4)
```
Answer: old

