Question: Is the toilet paper next to the toilet made of paper?

Reference Answer: yes

Image path: ./sampled_GQA/n417401.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='toilet paper')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='toilet')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What is the toilet made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'paper' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_NEXTTO'

