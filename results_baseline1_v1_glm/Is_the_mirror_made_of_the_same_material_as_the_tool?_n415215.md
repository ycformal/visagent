Question: Is the mirror made of the same material as the tool?

Reference Answer: no

Image path: ./sampled_GQA/n415215.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='mirror')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='material')
IMAGE1=CROP(image=IMAGE,object='tool')
BOX2=LOC(image=IMAGE1,object='material')
ANSWER0=VQA(image=IMAGE0,question='What is the {BOX1} of the {BOX0}?')
ANSWER1=VQA(image=IMAGE1,question='What is the {BOX2} of the {BOX0}?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'box'

