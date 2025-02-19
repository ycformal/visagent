Question: What is the vehicle that is made of same material as the pole that is not short called?

Reference Answer: van

Image path: ./sampled_GQA/n256120.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='pole')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='vehicle')
ANSWER0=VQA(image=IMAGE0,question='What material is the pole made of?')
ANSWER1=VQA(image=IMAGE0,question='What material is the vehicle made of?')
ANSWER2=VQA(image=IMAGE0,question='What is the vehicle called?')
ANSWER3=EVAL(expr="'{ANSWER2} that is made of {ANSWER0} material as the {ANSWER1} pole'")
FINAL_RESULT=RESULT(var=ANSWER3)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

