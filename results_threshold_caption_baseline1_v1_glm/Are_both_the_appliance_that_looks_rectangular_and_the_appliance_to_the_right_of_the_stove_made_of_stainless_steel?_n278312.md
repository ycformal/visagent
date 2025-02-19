Question: Are both the appliance that looks rectangular and the appliance to the right of the stove made of stainless steel?

Reference Answer: yes

Image path: ./sampled_GQA/n278312.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='stove')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='appliance')
IMAGE1=CROP_LEFTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='appliance')
ANSWER0=VQA(image=BOX1,question='What material is the appliance made of?')
ANSWER1=VQA(image=BOX2,question='What material is the appliance made of?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} =='stainless steel' and {ANSWER1} =='stainless steel' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: No.

