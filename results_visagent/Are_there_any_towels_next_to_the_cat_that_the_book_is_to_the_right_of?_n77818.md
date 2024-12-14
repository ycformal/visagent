Question: Are there any towels next to the cat that the book is to the right of?

Reference Answer: Yes, there are towels next to the cat.

Image path: ./sampled_GQA/n77818.jpg

Program:

```
 Are there any As next to B?
Program:
BOX0=LOC(image=IMAGE,object='cat')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='book')
IMAGE1=CROP_RIGHTOF(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE,object='towels')
IMAGE2=CROP_NEAR(image=IMAGE,box=BOX2)
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: yes

