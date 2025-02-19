Question: How old is the girl that is wearing a sweatshirt?

Reference Answer: young

Image path: ./sampled_GQA/n159802.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='girl')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='How old is the girl?')
ANSWER1=EVAL(expr="'unknown' if {ANSWER0} == 'unknown' else {ANSWER0} + ' years old'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: "runtime error"

