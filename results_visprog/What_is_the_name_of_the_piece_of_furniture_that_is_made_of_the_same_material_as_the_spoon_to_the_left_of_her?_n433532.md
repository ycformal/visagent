Question: What is the name of the piece of furniture that is made of the same material as the spoon to the left of her?

Reference Answer: The piece of furniture is a shelf.

Image path: ./sampled_GQA/n433532.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='spoon')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the spoon made of?')
BOX1=LOC(image=IMAGE,object=ANSWER0)
ANSWER1=VQA(image=IMAGE,question='What is the name of the piece of furniture?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: name 'ANSWER0' is not defined

