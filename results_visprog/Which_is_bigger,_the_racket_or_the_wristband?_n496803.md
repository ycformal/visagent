Question: Which is bigger, the racket or the wristband?

Reference Answer: The racket is bigger than the wristband.

Image path: ./sampled_GQA/n496803.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='racket')
BOX1=LOC(image=IMAGE,object='wristband')
IMAGE0=CROP(image=IMAGE,box=BOX0)
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=SIZE(image=IMAGE0)
ANSWER1=SIZE(image=IMAGE1)
ANSWER2=EVAL(expr="'racket' if {ANSWER0} > {ANSWER1} else 'wristband'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'SIZE'

