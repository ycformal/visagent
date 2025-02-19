Question: Are there any red fire trucks?

Reference Answer: no

Image path: ./sampled_GQA/n309148.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='fire truck')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes.

