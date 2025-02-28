Question: Was this photo taken in the 21st century?

Reference Answer: no

Image path: ./sampled_GQA/376247.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='When was this photo taken?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} >= 2000 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: '>=' not supported between instances of 'str' and 'int'

