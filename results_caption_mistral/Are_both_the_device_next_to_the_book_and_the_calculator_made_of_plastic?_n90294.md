Question: Are both the device next to the book and the calculator made of plastic?

Reference Answer: yes

Image path: ./sampled_GQA/n90294.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='book')
IMAGE0=CROP_NEXTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='device')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE,object='calculator')
IMAGE2=CROP(image=IMAGE,box=BOX2)
ANSWER0=VQA(image=IMAGE1,question='Is the device made of plastic?')
ANSWER1=VQA(image=IMAGE2,question='Is the calculator made of plastic?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'yes' and {ANSWER1} == 'yes' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: "runtime error"

