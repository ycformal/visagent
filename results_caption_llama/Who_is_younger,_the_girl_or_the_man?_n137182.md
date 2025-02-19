Question: Who is younger, the girl or the man?

Reference Answer: girl

Image path: ./sampled_GQA/n137182.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='girl')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='man')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='How old is the girl?')
ANSWER1=VQA(image=IMAGE1,question='How old is the man?')
ANSWER2=EVAL(expr="'girl' if {ANSWER0} < {ANSWER1} else'man'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: "runtime error"

