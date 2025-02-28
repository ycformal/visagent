Question: Where are the luggage?

Reference Answer: on belt

Image path: ./sampled_GQA/270274.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='luggage')
ANSWER0=EVAL(expr="'left' if {BOX0.x} < IMAGE.width/2 else 'right'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'list' object has no attribute 'x'

