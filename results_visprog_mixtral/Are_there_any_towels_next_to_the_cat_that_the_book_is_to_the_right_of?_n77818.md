Question: Are there any towels next to the cat that the book is to the right of?

Reference Answer: yes

Image path: ./sampled_GQA/n77818.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='book')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='cat')
IMAGE1=CROP_NEXTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='towels')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_NEXTOF'

