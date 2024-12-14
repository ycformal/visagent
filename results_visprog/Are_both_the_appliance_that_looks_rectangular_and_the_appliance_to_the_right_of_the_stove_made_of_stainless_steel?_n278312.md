Question: Are both the appliance that looks rectangular and the appliance to the right of the stove made of stainless steel?

Reference Answer: Yes, both the microwave oven and the toaster are made of stainless steel.

Image path: ./sampled_GQA/n278312.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='stove')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='appliance')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='rectangular')
IMAGE2=CROP(image=IMAGE1,box=BOX2)
BOX3=LOC(image=IMAGE0,object='appliance')
IMAGE3=CROP_RIGHTOF(image=IMAGE0,box=BOX3)
BOX4=LOC(image=IMAGE3,object='stainless steel')
ANSWER0=VQA(image=IMAGE2,question='What material is the appliance made of?')
ANSWER1=VQA(image=IMAGE4,question='What material is the appliance made of?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'stainless steel' and {ANSWER1} == 'stainless steel' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'IMAGE4'

