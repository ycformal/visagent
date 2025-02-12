Question: Is the racket on the left?

Reference Answer: no

Image path: ./sampled_GQA/n51658.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='racket')
ANSWER0=EVAL(expr="'yes' if {BOX0[0]} < 0.5 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: '<' not supported between instances of 'list' and 'float'

