Question: How is the item of furniture that is the same color as the device that is above the keyboard called?

Reference Answer: office chair

Image path: ./sampled_GQA/n525901.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='keyboard')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='device')
IMAGE1=CROP_ABOVE(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='item of furniture')
ANSWER0=VQA(image=IMAGE1,question='What color is the item of furniture?')
ANSWER1=VQA(image=IMAGE0,question='What color is the device?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
BOX0=LOC(image=IMAGE,object='keyboard')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='device')
IMAGE1=CROP_ABOVE(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='item of furniture')
ANSWER0=VQA(image=IMAGE1,question='What color is the item of furniture?')
ANSWER1=VQA(image=IMAGE0,question='What color is the device?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: desk

