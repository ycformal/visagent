Question: Is the knife on the left?

Reference Answer: no

Image path: ./sampled_GQA/n312206.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='knife')
ANSWER0=EVAL(expr="'yes' if {BOX0[0]} < {IMAGE.width}/2 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: '<' not supported between instances of 'list' and 'float'

