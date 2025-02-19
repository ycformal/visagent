Question: What is the dessert that is the same shape as the large container called?

Reference Answer: brownie

Image path: ./sampled_GQA/n28996.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='large container')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='dessert')
ANSWER0=VQA(image=IMAGE0,question='What shape is the large container?')
ANSWER1=VQA(image=IMAGE0,question='What shape is the dessert?')
ANSWER2=EVAL(expr="'{ANSWER1}' if {ANSWER0} == 'same' else 'none'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
BOX0=LOC(image=IMAGE,object='large container')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='dessert')
ANSWER0=VQA(image=IMAGE0,question='What shape is the large container?')
ANSWER1=VQA(image=IMAGE0,question='What shape is the dessert?')
ANSWER2=EVAL(expr="'{ANSWER1}' if {ANSWER0} == 'same' else 'none'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: cake

