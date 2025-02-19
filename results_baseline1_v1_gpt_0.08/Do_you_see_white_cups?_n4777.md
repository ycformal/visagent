Question: Do you see white cups?

Reference Answer: yes

Image path: ./sampled_GQA/n4777.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cups')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

