Question: How is the sign that is the same color as the chimney called?

Reference Answer: street sign

Image path: ./sampled_GQA/n173807.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='chimney')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the chimney?')
ANSWER1=EVAL(expr="'{ANSWER0}'")
BOX1=LOC(image=IMAGE,object='sign')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER2=VQA(image=IMAGE1,question='What color is the sign?')
ANSWER3=EVAL(expr="'{ANSWER2}'")
ANSWER4=EVAL(expr="'yes' if {ANSWER1} == {ANSWER3} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER4)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

