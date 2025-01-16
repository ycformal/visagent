Question: Which is bigger, the racket or the wristband?

Reference Answer: The racket is bigger than the wristband.

Image path: ./sampled_GQA/n496803.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='racket')
BOX1=LOC(image=IMAGE,object='wristband')
ANSWER0=SIZE(box=BOX0)
ANSWER1=SIZE(box=BOX1)
ANSWER2=EVAL(expr="'racket' if {ANSWER0} > {ANSWER1} else 'wristband'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: none

