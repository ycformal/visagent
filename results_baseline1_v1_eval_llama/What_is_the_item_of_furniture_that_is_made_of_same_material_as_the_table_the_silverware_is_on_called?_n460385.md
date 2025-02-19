Question: What is the item of furniture that is made of same material as the table the silverware is on called?

Reference Answer: shelf

Image path: ./sampled_GQA/n460385.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='table')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='silverware')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='furniture')
ANSWER0=VQA(image=IMAGE1,question='What material is the silverware made of?')
ANSWER1=VQA(image=IMAGE0,question='What material is the table made of?')
ANSWER2=EVAL(expr="'{ANSWER0}' if {ANSWER1} == {ANSWER0} else 'unknown'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

