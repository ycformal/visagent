Question: What type of furniture has the same color as the soccer ball?

Reference Answer: chair

Image path: ./sampled_GQA/n350732.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='soccer ball')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the soccer ball?')
BOX1=LOC(image=IMAGE,object=ANSWER0)
ANSWER1=VQA(image=IMAGE,question='What type of furniture is the {ANSWER0}?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: name 'ANSWER0' is not defined

