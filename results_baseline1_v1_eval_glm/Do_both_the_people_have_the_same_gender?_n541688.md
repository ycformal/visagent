Question: Do both the people have the same gender?

Reference Answer: no

Image path: ./sampled_GQA/n541688.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='people')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='people')
ANSWER0=VQA(image=IMAGE0,question='What is the gender of the people?')
ANSWER1=VQA(image=IMAGE1,question='What is the gender of the people?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'IMAGE1'

