Question: How is the piece of furniture that is made of same material as the brown chair called?

Reference Answer: side table

Image path: ./sampled_GQA/n83784.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='brown chair')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='piece of furniture')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='same material')
ANSWER0=VQA(image=IMAGE1,question='What is the piece of furniture made of?')
ANSWER1=VQA(image=IMAGE1,question='What is the brown chair made of?')
ANSWER2=EVAL(expr="'{ANSWER0}' if {ANSWER1} == 'brown' else 'unknown'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

