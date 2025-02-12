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
BOX3=LOC(image=IMAGE2,object='umbrella')
ANSWER0=VQA(image=IMAGE3,question='What color is the umbrella?')
ANSWER1=VQA(image=IMAGE2,question='What color is the furniture?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'IMAGE3'

