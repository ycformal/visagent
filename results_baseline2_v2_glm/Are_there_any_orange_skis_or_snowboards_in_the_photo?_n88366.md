Question: Are there any orange skis or snowboards in the photo?

Reference Answer: no

Image path: ./sampled_GQA/n88366.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='ski')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the ski?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'orange' else 'no'")
ANSWER2=LOC(image=IMAGE,object='snowboard')
ANSWER3=VQA(image=ANSWER2,question='What color is the snowboard?')
ANSWER4=EVAL(expr="'yes' if {ANSWER3} == 'orange' else 'no'")
ANSWER5=EVAL(expr="'yes' if {ANSWER1} == 'yes' or {ANSWER4} == 'yes' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER5)
```
Program:

```
BOX0=LOC(image=IMAGE,object='ski',plural=True)
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the ski?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'orange' else 'no'")
ANSWER2=LOC(image=IMAGE,object='snowboard',plural=True)
ANSWER3=VQA(image=ANSWER2,question='What color is the snowboard?')
ANSWER4=EVAL(expr="'yes' if {ANSWER3} == 'orange' else 'no'")
ANSWER5=EVAL(expr="'yes' if {ANSWER1} == True or {ANSWER4} == True else 'no'")
FINAL_RESULT=RESULT(var=ANSWER5)
```
Answer: skis

