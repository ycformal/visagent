Question: How is the piece of furniture that is made of same material as the wall called?

Reference Answer: The piece of furniture is a table.

Image path: ./sampled_GQA/2388805.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='wall')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='furniture')
ANSWER0=VQA(image=IMAGE0,question='What material is the wall made of?')
ANSWER1=VQA(image=IMAGE0,question='What is the name of the furniture?')
ANSWER2=EVAL(expr="'{ANSWER1}' if {ANSWER0} in {ANSWER1} else 'unknown'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

