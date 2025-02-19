Question: Are both the white thing to the right of the chair and the toilet paper to the right of the toilet made of paper?

Reference Answer: yes

Image path: ./sampled_GQA/n59147.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='chair')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='white thing')
ANSWER0=VQA(image=IMAGE1,question='What is the white thing to the right of the chair made of?')
BOX2=LOC(image=IMAGE,object='toilet')
IMAGE1=CROP_RIGHTOF(image=IMAGE,box=BOX2)
BOX3=LOC(image=IMAGE1,object='toilet paper')
ANSWER1=VQA(image=IMAGE1,question='What is the toilet paper to the right of the toilet made of?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'paper' and {ANSWER1} == 'paper' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: "runtime error"

