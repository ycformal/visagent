Question: What do both the window and the jar have in common?

Reference Answer: material

Image path: ./sampled_GQA/n578564.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='window')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='jar')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='What color is the window?')
ANSWER1=VQA(image=IMAGE1,question='What color is the jar?')
ANSWER2=EVAL(expr="'both are {ANSWER0}' if {ANSWER0} == {ANSWER1} else 'both are not {ANSWER0}'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

