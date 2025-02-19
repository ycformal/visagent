Question: Is there a bird in the picture that is not large?

Reference Answer: yes

Image path: ./sampled_GQA/n477215.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bird')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: "runtime error"

