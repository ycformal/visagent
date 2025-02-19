Question: What is the name of the piece of furniture that is made of the same material as the pepper grinder on the right?

Reference Answer: entertainment center

Image path: ./sampled_GQA/n77818.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='RIGHT')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='pepper grinder')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What material is this?')
ANSWER1=VQA(image=IMAGE,question='What is the name of the piece of furniture?')
ANSWER2=EVAL(expr="if {ANSWER0} == {ANSWER1} then 'yes' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: runtime error

