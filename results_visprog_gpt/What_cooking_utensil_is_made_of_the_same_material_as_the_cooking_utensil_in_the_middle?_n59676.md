Question: What cooking utensil is made of the same material as the cooking utensil in the middle?

Reference Answer: pan

Image path: ./sampled_GQA/n59676.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='middle')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='cooking utensil')
ANSWER0=VQA(image=IMAGE0,question='What material is the cooking utensil made of?')
ANSWER1=VQA(image=IMAGE,question='What material is the cooking utensil in the middle made of?')
ANSWER2=EVAL(expr="'The same material as the cooking utensil in the middle is {ANSWER0}' if {ANSWER0} == {ANSWER1} else 'The cooking utensil in the middle is made of a different material'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

