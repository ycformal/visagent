Question: What is the color of the cooking utensil made of metal?

Reference Answer: blue

Image path: ./sampled_GQA/n578564.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='metal')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='cooking utensil')
ANSWER0=VQA(image=IMAGE1,question='What color is the cooking utensil?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: "runtime error"

