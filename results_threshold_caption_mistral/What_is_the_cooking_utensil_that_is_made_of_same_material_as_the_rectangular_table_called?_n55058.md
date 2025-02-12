Question: What is the cooking utensil that is made of same material as the rectangular table called?

Reference Answer: cutting board

Image path: ./sampled_GQA/n55058.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='rectangular table')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the rectangular table made of?')
ANSWER1=EVAL(expr="'{ANSWER0}'")
BOX1=LOC(image=IMAGE,object='cooking utensil')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER2=VQA(image=IMAGE1,question='What is the cooking utensil made of?')
ANSWER3=EVAL(expr="'yes' if {ANSWER0} == {ANSWER2} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER3)
```
Answer: spatula

