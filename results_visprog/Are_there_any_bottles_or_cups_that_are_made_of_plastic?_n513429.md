Question: Are there any bottles or cups that are made of plastic?

Reference Answer: No, there is a bottle but it is made of glass.

Image path: ./sampled_GQA/n513429.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bottle')
BOX1=LOC(image=IMAGE,object='cup')
ANSWER0=COUNT(box=BOX0)
ANSWER1=COUNT(box=BOX1)
ANSWER2=EVAL(expr="'yes' if {ANSWER0} + {ANSWER1} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

