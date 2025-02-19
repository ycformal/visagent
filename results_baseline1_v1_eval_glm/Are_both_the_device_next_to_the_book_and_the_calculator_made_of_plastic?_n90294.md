Question: Are both the device next to the book and the calculator made of plastic?

Reference Answer: yes

Image path: ./sampled_GQA/n90294.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='book')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='device')
IMAGE1=CROP_NEXTTO(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='calculator')
ANSWER0=VQA(image=BOX1,question='What material is the device made of?')
ANSWER1=VQA(image=BOX2,question='What material is the calculator made of?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'plastic' and {ANSWER1} == 'plastic' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'CROP_NEXTTO'

