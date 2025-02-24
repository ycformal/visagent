Question: Does the shelf to the right of the other shelf have white color?

Reference Answer: yes

Image path: ./sampled_GQA/n119886.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='shelf')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='shelf')
ANSWER0=VQA(image=IMAGE1,question='What color is the shelf?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'white' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'IMAGE1'

