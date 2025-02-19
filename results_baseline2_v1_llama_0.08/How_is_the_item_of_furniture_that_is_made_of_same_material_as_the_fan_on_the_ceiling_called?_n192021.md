Question: How is the item of furniture that is made of same material as the fan on the ceiling called?

Reference Answer: table

Image path: ./sampled_GQA/n192021.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='fan')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='item of furniture')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='material')
IMAGE2=CROP_BELOW(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='fan')
ANSWER0=VQA(image=IMAGE0,question='What is the item of furniture called?')
ANSWER1=VQA(image=IMAGE2,question='What is the fan called?')
ANSWER2=EVAL(expr="'{ANSWER0}' if {ANSWER1} == 'fan' else 'no match'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
BOX0=LOC(image=IMAGE,object='fan')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='item of furniture')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='material')
IMAGE2=CROP_BELOW(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE2,object='fan')
ANSWER0=VQA(image=IMAGE0,question='What is the item of furniture called?')
ANSWER1=VQA(image=IMAGE2,question='What is the fan called?')
ANSWER2=EVAL(expr="'{ANSWER0}' if {ANSWER1} == 'fan' else 'no match'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: fan

