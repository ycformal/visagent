Question: Is everyone wearing a helmet?

Reference Answer: yes

Image path: ./sampled_GQA/485896.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='helmet')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == {COUNT(box=BOX0)} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'COUNT(box=BOX0)'

