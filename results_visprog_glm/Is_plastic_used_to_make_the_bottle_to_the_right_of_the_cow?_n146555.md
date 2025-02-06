Question: Is plastic used to make the bottle to the right of the cow?

Reference Answer: yes

Image path: ./sampled_GQA/n146555.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='RIGHT')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='cow')
IMAGE1=CROP_LEFTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='bottle')
ANSWER0=VQA(image=IMAGE2,question='What is the bottle made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'plastic' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'IMAGE2'

