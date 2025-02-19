Question: Is there a bottle to the right of the old person that wears shoes?

Reference Answer: no

Image path: ./sampled_GQA/n151768.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='old person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Is the old person wearing shoes?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'yes' else 'no'")
ANSWER2=EVAL(expr="'yes' if {ANSWER1} == 'yes' else 'no'")
ANSWER3=EVAL(expr="'yes' if {ANSWER2} == 'yes' else 'no'")
ANSWER4=EVAL(expr="'yes' if {ANSWER3} == 'yes' else 'no'")
ANSWER5=EVAL(expr="'yes' if {ANSWER4} == 'yes' else 'no'")
ANSWER6=EVAL(expr="'yes' if {ANSWER5} == 'yes' else 'no'")
ANSWER7=EVAL(expr="'yes' if {ANSWER6} == 'yes' else 'no'")
ANSWER8=EVAL(expr
```
Answer: Runtime error: ('EOF in multi-line statement', (2, 0))

