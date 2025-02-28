Question: Where are the people?

Reference Answer: school

Image path: ./sampled_GQA/432547.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='people')
ANSWER0=EVAL(expr="'inside' if {BOX0} > 0 else 'outside'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: '>' not supported between instances of 'list' and 'int'

