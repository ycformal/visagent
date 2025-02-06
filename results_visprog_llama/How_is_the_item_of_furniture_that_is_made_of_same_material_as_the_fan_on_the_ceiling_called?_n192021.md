Question: How is the item of furniture that is made of same material as the fan on the ceiling called?

Reference Answer: table

Image path: ./sampled_GQA/n192021.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='fan')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='item of furniture')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='material')
IMAGE2=CROP(image=IMAGE,box=BOX2)
ANSWER0=VQA(image=IMAGE2,question='What is the item of furniture made of?')
ANSWER1=VQA(image=IMAGE0,question='What is the fan made of?')
ANSWER2=EVAL(expr="'{ANSWER0}' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

