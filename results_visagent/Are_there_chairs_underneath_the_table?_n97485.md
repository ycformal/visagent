Question: Are there chairs underneath the table?

Reference Answer: Yes, there is a chair underneath the table.

Image path: ./sampled_GQA/n97485.jpg

Program:

```
 Are A <spatial pos> B?
Program:
BOX0=LOC(image=IMAGE,object='table')
IMAGE0=CROP_UNDER(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='chair')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: no

