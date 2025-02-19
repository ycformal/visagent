Question: What cooking utensil is made of the same material as the cooking utensil in the middle?

Reference Answer: pan

Image path: ./sampled_GQA/n59676.jpg

Program:

```
BOX0=EVAL(expr="[[0,0,{IMAGE.size[0]}-1,{IMAGE.size[1]}-1]]")
IMAGE0=CROP_MIDDLE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='cooking utensil')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What material is the cooking utensil made of?')
ANSWER1=VQA(image=IMAGE,question='What cooking utensil is made of {ANSWER0}?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_MIDDLE'

