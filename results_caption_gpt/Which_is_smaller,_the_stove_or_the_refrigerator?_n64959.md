Question: Which is smaller, the stove or the refrigerator?

Reference Answer: stove

Image path: ./sampled_GQA/n64959.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='stove')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='refrigerator')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=SIZE(image=IMAGE0)
ANSWER1=SIZE(image=IMAGE1)
ANSWER2=EVAL(expr="'stove' if {ANSWER0} < {ANSWER1} else 'refrigerator'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: "runtime error"

