Question: What device is to the left of the calculator made of plastic?

Reference Answer: charger

Image path: ./sampled_GQA/n90294.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='calculator')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the calculator made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'plastic' else 'no'")
ANSWER2=EVAL(expr="'yes' if {ANSWER1} == 'yes' else 'no'")
ANSWER3=EVAL(expr="'yes' if {ANSWER2} == 'yes' else 'no'")
ANSWER4=EVAL(expr="'yes' if {ANSWER3} == 'yes' else 'no'")
ANSWER5=EVAL(expr="'yes' if {ANSWER4} == 'yes' else 'no'")
ANSWER6=EVAL(expr="'yes' if {ANSWER5} == 'yes' else 'no'")
ANSWER7=EVAL(expr="'yes' if {ANSWER6} == 'yes' else 'no'")
ANSWER8=EVAL(ex
```
Answer: mouse

