Question: What do both the net and the fence have in common?

Reference Answer: color

Image path: ./sampled_GQA/n282607.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='net')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='fence')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='What color is the net?')
ANSWER1=VQA(image=IMAGE1,question='What color is the fence?')
ANSWER2=EVAL(expr="'both are {ANSWER0}' if {ANSWER0} == {ANSWER1} else 'both are not {ANSWER0}'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
BOX0=LOC(image=IMAGE,object='net')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='fence')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='What color is the net?')
ANSWER1=VQA(image=IMAGE1,question='What color is the fence?')
ANSWER2=EVAL(expr="'both are {ANSWER0}' if {ANSWER0} == {ANSWER1} else 'both are not {ANSWER0}'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: black

