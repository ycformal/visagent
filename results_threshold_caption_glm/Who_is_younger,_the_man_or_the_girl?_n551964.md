Question: Who is younger, the man or the girl?

Reference Answer: girl

Image path: ./sampled_GQA/n551964.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='girl')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='How old is the girl?')
BOX1=LOC(image=IMAGE,object='man')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER1=VQA(image=IMAGE1,question='How old is the man?')
ANSWER2=EVAL(expr="'girl' if {ANSWER0} < {ANSWER1} else'man'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: boy

