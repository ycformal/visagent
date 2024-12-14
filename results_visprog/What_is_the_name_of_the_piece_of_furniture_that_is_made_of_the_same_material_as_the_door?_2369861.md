Question: What is the name of the piece of furniture that is made of the same material as the door?

Reference Answer: The piece of furniture is a drawer.

Image path: ./sampled_GQA/2369861.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='door')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the door made of?')
BOX1=LOC(image=IMAGE,object=ANSWER0)
ANSWER1=VQA(image=IMAGE,question='What is the name of the piece of furniture?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: name 'ANSWER0' is not defined

