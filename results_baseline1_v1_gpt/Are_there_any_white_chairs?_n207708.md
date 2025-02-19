Question: Are there any white chairs?

Reference Answer: no

Image path: ./sampled_GQA/n207708.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='chair')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

