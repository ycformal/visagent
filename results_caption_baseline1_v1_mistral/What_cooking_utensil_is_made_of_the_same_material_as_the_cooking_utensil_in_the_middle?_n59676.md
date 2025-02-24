Question: What cooking utensil is made of the same material as the cooking utensil in the middle?

Reference Answer: pan

Image path: ./sampled_GQA/n59676.jpg

Program:

```
BOX0=GET(image=IMAGE)
IMAGE0=CROP_MIDDLE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='cooking utensil')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What cooking utensil is made of the same material as the cooking utensil in the middle?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_MIDDLE'

