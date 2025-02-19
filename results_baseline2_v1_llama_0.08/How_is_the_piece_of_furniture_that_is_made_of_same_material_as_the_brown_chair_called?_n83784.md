Question: How is the piece of furniture that is made of same material as the brown chair called?

Reference Answer: side table

Image path: ./sampled_GQA/n83784.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='brown chair')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='piece of furniture')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What color is the piece of furniture?')
ANSWER1=VQA(image=IMAGE1,question='What material is the piece of furniture made of?')
ANSWER2=EVAL(expr="'{ANSWER0} {ANSWER1}'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
BOX0=LOC(image=IMAGE,object='brown chair')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='piece of furniture')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What color is the piece of furniture?')
ANSWER1=VQA(image=IMAGE1,question='What material is the piece of furniture made of?')
ANSWER2=EVAL(expr="'{ANSWER0} {ANSWER1}'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: chair

