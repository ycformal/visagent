Question: Which seems to be younger, the girl or the man?

Reference Answer: The girl is younger than the man.

Image path: ./sampled_GQA/n498712.jpg

Program:

```
Which seems to be younger, A or B?
Program:
BOX0=LOC(image=IMAGE,object='girl')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='man')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='What is the age of the girl?')
ANSWER1=VQA(image=IMAGE1,question='What is the age of the man?')
ANSWER2=EVAL(expr="'girl' if {ANSWER0} < {ANSWER1} else 'man'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: woman

