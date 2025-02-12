Question: How is the piece of furniture that is the same color as the umbrella that is to the left of the person called?

Reference Answer: cabinet

Image path: ./sampled_GQA/n507959.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='LEFT')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='umbrella')
IMAGE1=CROP_LEFTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='furniture')
ANSWER0=VQA(image=IMAGE2,question='What is the piece of furniture that is the same color as the umbrella that is to the left of the person called?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'IMAGE2'

