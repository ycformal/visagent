Question: Are there birds next to the towels?

Reference Answer: No, there is a cat next to the towels.

Image path: ./sampled_GQA/n77818.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='towels')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='birds')
IMAGE1=CROP_NEAR(image=IMAGE0,box=BOX1)
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_NEAR'

