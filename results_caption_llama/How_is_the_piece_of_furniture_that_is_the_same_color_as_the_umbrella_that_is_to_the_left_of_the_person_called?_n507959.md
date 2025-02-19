Question: How is the piece of furniture that is the same color as the umbrella that is to the left of the person called?

Reference Answer: cabinet

Image path: ./sampled_GQA/n507959.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='umbrella')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='furniture')
IMAGE2=CROP(image=IMAGE,box=BOX2)
BOX3=LOC(image=IMAGE2,object='furniture')
IMAGE3=CROP(image=IMAGE,box=BOX3)
ANSWER0=VQA(image=IMAGE3,question='What color is the piece of furniture?')
ANSWER1=VQA(image=IMAGE2,question='What color is the umbrella?')
ANSWER2=EVAL(expr="'{ANSWER0}' if {ANSWER1} == {ANSWER0} else 'unknown'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: runtime error

