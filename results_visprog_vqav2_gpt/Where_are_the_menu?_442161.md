Question: Where are the menu?

Reference Answer: on table

Image path: ./sampled_GQA/442161.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='menu')
ANSWER0=EVAL(expr="'top' if {BOX0[0]} < 0.5 else 'bottom'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: '<' not supported between instances of 'list' and 'float'

