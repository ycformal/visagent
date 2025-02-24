Question: What is the vehicle that is made of same material as the pole that is not short called?

Reference Answer: van

Image path: ./sampled_GQA/n256120.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='pole')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Is the pole short?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'no' else 'no'")
BOX1=LOC(image=IMAGE,object='vehicle')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER2=VQA(image=IMAGE1,question='What is the vehicle made of?')
ANSWER3=VQA(image=IMAGE0,question='What is the pole made of?')
ANSWER4=EVAL(expr="'yes' if {ANSWER2} == {ANSWER3} else 'no'")
ANSWER5=EVAL(expr="'yes' if {ANSWER1} == 'yes' and {ANSWER4} == 'yes' else 'no'")
ANSWER6=EVAL(expr="'yes' if {ANSWER5} == 'yes' else 'no'")
FINAL_RESULT=RESULT(var=ANSW
```
Answer: Runtime error: ('EOF in multi-line statement', (2, 0))

