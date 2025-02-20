Question: How is the item of furniture that is made of same material as the floor called?

Reference Answer: bookcase

Image path: ./sampled_GQA/n69237.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='floor')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='item of furniture')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What is the item of furniture made of?')
ANSWER1=VQA(image=IMAGE0,question='What is the floor made of?')
ANSWER2=EVAL(expr="'{ANSWER0}' if {ANSWER0} == {ANSWER1} else 'unknown'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
BOX0=LOC(image=IMAGE,object='floor')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='item of furniture')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What is the item of furniture made of?')
ANSWER1=VQA(image=IMAGE0,question='What is the floor made of?')
ANSWER2=EVAL(expr="'{ANSWER0}' if {ANSWER0} == {ANSWER1} else 'unknown'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: bed

