Question: What kind of sign is made of the same material as the vehicle next to the sidewalk?

Reference Answer: street sign

Image path: ./sampled_GQA/n311910.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='sidewalk')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='vehicle')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE,object='sign')
IMAGE2=CROP(image=IMAGE,box=BOX2)
ANSWER0=VQA(image=IMAGE1,question='What material is the vehicle made of?')
ANSWER1=VQA(image=IMAGE2,question='What material is the sign made of?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: runtime error

