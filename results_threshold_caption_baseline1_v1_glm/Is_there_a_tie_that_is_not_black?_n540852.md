Question: Is there a tie that is not black?

Reference Answer: no

Image path: ./sampled_GQA/n540852.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='tie')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes

