Question: What is the name of the cooking utensil that is made of the same material as the stick?

Reference Answer: The cooking utensil is a spatula.

Image path: ./sampled_GQA/2391016.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='stick')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the stick made of?')
BOX1=LOC(image=IMAGE,object='cooking utensil')
IMAGE1=CROP_SAME_MATERIAL(image=IMAGE,box=BOX1,material=ANSWER0)
ANSWER1=VQA(image=IMAGE1,question='What is the name of the cooking utensil?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: wood

