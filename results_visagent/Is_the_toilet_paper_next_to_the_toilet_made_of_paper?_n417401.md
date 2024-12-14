Question: Is the toilet paper next to the toilet made of paper?

Reference Answer: Yes, the toilet paper is made of paper.

Image path: ./sampled_GQA/n417401.jpg

Program:

```
 Is A <spatial pos> B made of <material>?
Program:
BOX0=LOC(image=IMAGE,object='toilet')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='toilet paper')
IMAGE1=CROP_NEXTTO(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE1,question='What material is the toilet paper made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'paper' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: yes

