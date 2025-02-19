Question: How is the piece of furniture that is the same color as the umbrella that is to the left of the person called?

Reference Answer: cabinet

Image path: ./sampled_GQA/n507959.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='umbrella')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What color is the umbrella?')
ANSWER1=EVAL(expr="'{ANSWER0}'")
BOX2=LOC(image=IMAGE,object='{ANSWER1}')
IMAGE2=CROP(image=IMAGE,box=BOX2)
ANSWER2=VQA(image=IMAGE2,question='How is the piece of furniture called?')
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: runtime error

