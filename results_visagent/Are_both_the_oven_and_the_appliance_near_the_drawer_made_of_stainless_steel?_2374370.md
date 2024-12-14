Question: Are both the oven and the appliance near the drawer made of stainless steel?

Reference Answer: Yes, both the oven and the stove are made of stainless steel.

Image path: ./sampled_GQA/2374370.jpg

Program:

```
 Are both A and B near C made of <material>?
Program:
BOX0=LOC(image=IMAGE,object='drawer')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='oven')
IMAGE1=CROP_NEAR(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE,object='appliance')
IMAGE2=CROP_NEAR(image=IMAGE0,box=BOX2)
ANSWER0=VQA(image=IMAGE1,question='What material is the oven made of?')
ANSWER1=VQA(image=IMAGE2,question='What material is the appliance made of?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'stainless steel' and {ANSWER1} == 'stainless steel' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: yes

