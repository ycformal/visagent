Question: Is the pitcher that is not old wearing a glove?

Reference Answer: no

Image path: ./sampled_GQA/n485969.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='pitcher')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='glove')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

