Question: Where are the goggles?

Reference Answer: on her head

Image path: ./sampled_GQA/451511.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='goggles')
ANSWER0=EVAL(expr="'top' if {BOX0} < 0.5 else 'bottom'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: '<' not supported between instances of 'list' and 'float'

