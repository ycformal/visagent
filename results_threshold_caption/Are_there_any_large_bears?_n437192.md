Question: Are there any large bears?

Reference Answer: Yes, there is a large bear.

Image path: ./sampled_GQA/n437192.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bear')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes
