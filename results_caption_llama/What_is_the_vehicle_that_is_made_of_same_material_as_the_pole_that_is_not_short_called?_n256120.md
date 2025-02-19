Question: What is the vehicle that is made of same material as the pole that is not short called?

Reference Answer: van

Image path: ./sampled_GQA/n256120.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='pole')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='short')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='vehicle')
IMAGE2=CROP(image=IMAGE,box=BOX2)
BOX3=LOC(image=IMAGE2,object='material')
ANSWER0=VQA(image=IMAGE0,question='What material is the pole made of?')
ANSWER1=VQA(image=IMAGE1,question='What material is the short made of?')
ANSWER2=VQA(image=IMAGE2,question='What material is the vehicle made of?')
ANSWER3=EVAL(expr="'{ANSWER0}' if {ANSWER1} =='short' else '{ANSWER2}'")
FINAL_RESULT=RESULT(var=ANSWER3)
```
Answer: runtime error

