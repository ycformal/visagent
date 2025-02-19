Question: Is plastic used to make the bottle to the right of the cow?

Reference Answer: yes

Image path: ./sampled_GQA/n146555.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cow')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='bottle')
ANSWER0=VQA(image=IMAGE1,question='What is the bottle made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'plastic' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'IMAGE1'

