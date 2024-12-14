Question: What cooking utensil is made of the same material as the cooking utensil in the middle?

Reference Answer: The pan is made of the same material as the spatula.

Image path: ./sampled_GQA/n59676.jpg

Program:

```
 What <attr> is A made of the same material as B?
Program:
BOX0=LOC(image=IMAGE,object='cooking utensil')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='cooking utensil')
IMAGE1=CROP_MIDDLE(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='What material is the cooking utensil made of?')
ANSWER1=VQA(image=IMAGE1,question='What material is the cooking utensil in the middle made of?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: spatula

