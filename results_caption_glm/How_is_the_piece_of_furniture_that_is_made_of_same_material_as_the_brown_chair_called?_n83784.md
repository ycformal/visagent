Question: How is the piece of furniture that is made of same material as the brown chair called?

Reference Answer: side table

Image path: ./sampled_GQA/n83784.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='chair')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the chair?')
ANSWER1=VQA(image=IMAGE0,question='What material is the chair made of?')
BOX1=LOC(image=IMAGE,object=ANSWER1)
ANSWER2=VQA(image=IMAGE,question='What is the piece of furniture that is made of {ANSWER1} called?')
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: runtime error

