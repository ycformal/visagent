Question: Are there lamps near the stacked books?

Reference Answer: Yes, there is a lamp near the books.

Image path: ./sampled_GQA/n432591.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='books')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='lamp')
IMAGE1=CROP_NEAR(image=IMAGE0,box=BOX1)
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_NEAR'

