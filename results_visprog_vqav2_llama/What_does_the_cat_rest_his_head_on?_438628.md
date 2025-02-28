Question: What does the cat rest his head on?

Reference Answer: keyboard

Image path: ./sampled_GQA/438628.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cat')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='mat')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

