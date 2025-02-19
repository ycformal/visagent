Question: What device is to the left of the calculator made of plastic?

Reference Answer: charger

Image path: ./sampled_GQA/n90294.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='calculator')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='device')
ANSWER0=VQA(image=IMAGE1,question='What material is the device made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'plastic' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'IMAGE1'

